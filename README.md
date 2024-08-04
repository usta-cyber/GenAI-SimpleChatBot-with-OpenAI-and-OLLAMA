# GenAI-SimpleChatBot-with-OpenAI-and-OLLAMA

# Chat Application using LangChain with OpenAI & OLLAMA

This repository contains a simple chat application that leverages LangChain to interface with both OpenAI's GPT-3.5-turbo model and the local Ollama LLaMA2 model. The application allows users to interact with these models seamlessly.

## Features

- **Chat with GPT-3.5-turbo:** Connects to OpenAI's GPT-3.5-turbo model for advanced conversational capabilities.
- **Chat with LLaMA2:** Utilizes the local Ollama LLaMA2 model for local AI processing.
- **Seamless Switching:** Easily switch between the two models during conversation.

## Screenshots
- OLLAMA
<img width="925" alt="ollama" src="https://github.com/user-attachments/assets/59a948fb-7958-47fe-8101-e0de72e16222">
- OPENAI
<img width="881" alt="openAI" src="https://github.com/user-attachments/assets/6ec6451d-294d-4bae-b858-9f885ff444ee">


## Installation

### Prerequisites

- Python 3.9
- OpenAI API key
- LangChain library
- Local setup for Ollama LLaMA2
- streamlit

### Setup

1. **Clone the repository:**
   ```bash
   https://github.com/usta-cyber/GenAI-SimpleChatBot-with-OpenAI-and-OLLAMA.git
   cd GenAI-SimpleChatBot-with-OpenAI-and-OLLAMA
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**

   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Configure LLaMA2:**

   Follow the instructions provided in the Ollama LLaMA2 documentation to set up the local model.

## Usage

1. **Run the application:**
- For OpenAI
   ```bash
   streamlit run chatBotOpenAIApp.py
   ```
- For Ollama
   ```bash
   streamlit run chatBotOllama.py
   ```
2. **Access the chat interface:**

   Open your web browser and navigate to `http://localhost:8501` to start chatting with the models.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [OpenAI](https://openai.com) for the GPT-3.5-turbo model.
- [LangChain](https://github.com/langchain/langchain) for the LangChain library.
- [Ollama](https://ollama.com) for the LLaMA2 model.
