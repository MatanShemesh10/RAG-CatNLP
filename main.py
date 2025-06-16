import ollama
from flask_cors import CORS
from flask import Flask, request, jsonify
import threading

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

# Load the dataset from a text file
dataset = []
with open('cat-facts.txt', encoding='utf-8') as file:
    dataset = file.readlines()
    print(f'Loaded {len(dataset)} entries')


# Each element in the VECTOR_DB will be a tuple (chunk, embedding)
# The embedding is a list of floats, for example: [0.1, 0.04, -0.34, 0.21, ...]
VECTOR_DB = []

def add_chunk_to_database(chunk):
  embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
  VECTOR_DB.append((chunk, embedding))

# Process each chunk and add it to the VECTOR_DB
# In this dataset, each line is a separate chunk
for i, chunk in enumerate(dataset):
  add_chunk_to_database(chunk)
  print(f'Added chunk {i+1}/{len(dataset)} to the database')

def cosine_similarity(a, b):
  dot_product = sum([x * y for x, y in zip(a, b)])
  norm_a = sum([x ** 2 for x in a]) ** 0.5
  norm_b = sum([x ** 2 for x in b]) ** 0.5
  return dot_product / (norm_a * norm_b)

def retrieve(query, top_n=3):
    print(f'\n>>> Received query: {query}')
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((chunk, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)

    print('\n>>> Retrieved knowledge:')
    for i, (chunk, sim) in enumerate(similarities[:top_n], 1):
        print(f'{i}. (similarity: {sim:.4f}) {chunk.strip()}')
    return similarities[:top_n]


app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    input_query = data.get('query', '')
    
    print(f'\n>>> Received query: {input_query}')
    
    retrieved_knowledge = retrieve(input_query)
    
    chunks_str = '\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])
    instruction_prompt = f'''You are a helpful chatbot.
    Use only the following pieces of context to answer the question. Don't make up any new information:
    {chunks_str}'''

    print('\n>>> Instruction prompt sent to the model:')
    print(instruction_prompt)

    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {'role': 'system', 'content': instruction_prompt},
            {'role': 'user', 'content': input_query},
        ],
        stream=True,
    )

    response = ''
    print('\n>>> Final chatbot response:')
    for chunk in stream:
        text = chunk['message']['content']
        print(text, end='', flush=True)
        response += text
    print()  # new line for cleanliness

    # return the response and the context used
    return jsonify({
        'response': response,
        'context_used': chunks_str
    })


def run_flask():
    app.run(port=5000, debug=True, use_reloader=False)

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()