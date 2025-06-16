# LLM Chat Project

This project implements a simple chatbot that provides interesting facts about cats using a local language model. The chatbot utilizes embeddings to retrieve relevant information based on user queries.

## Project Structure

- `main.py`: Contains the main logic for the LLM chat application. It handles loading the dataset, processing entries to create embeddings, and managing user interactions.
- `cat-facts.txt`: A dataset containing various facts about cats, with each line representing a separate fact.
- `README.md`: Documentation for the project, including setup and usage instructions.

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd llm-chat-project
   ```

2. **Install Dependencies**: 
   Ensure you have the `ollama` library installed. You can install it using pip:
   ```bash
   pip install ollama
   ```

3. **Prepare the Dataset**: 
   Make sure the `cat-facts.txt` file is present in the project directory. This file should contain one cat fact per line.

## Usage

To run the chatbot, execute the following command in your terminal:
```bash
python main.py
```

Once the chatbot is running, you can ask questions about cats, and it will respond with relevant facts from the dataset.

## Example Interaction

```
Welcome to the Cat Facts chatbot!
Ask me a question: What can you tell me about cats?
Retrieved knowledge:
 - (similarity: 0.85) Cats are known for their agility and grace.
 - (similarity: 0.80) A group of cats is called a clowder.
Chatbot response: Cats are fascinating creatures known for their agility and grace. A group of cats is called a clowder.
---
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or additional features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.