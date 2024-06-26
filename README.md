
## Project Overview

Jarvis is an AI-powered chatbot designed to assist users with scientific research and general knowledge queries. Leveraging the power of the Mixtral-8x7b-32768 model and integrating with ArXiv and Wikipedia, Jarvis provides intelligent, context-aware responses to user inquiries.

## Features

- AI-driven conversational interface
- ArXiv database integration for scientific paper queries
- Wikipedia integration for general knowledge
- Conversation memory for context-aware responses
- User-friendly Gradio web interface

## Technologies Used

- Python
- Gradio
- Langchain
- Groq API (Mixtral-8x7b-32768 model)
- ArXiv API
- Wikipedia API

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/rahulg-101/Jarvis-AI-Driven-arXiv-and-Wikipedia-Query-Chatbot-using-Langchain.git
   
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Run the application:
```
python arxivchatbot.py
```

Open your web browser and navigate to the URL provided by Gradio (usually `http://127.0.0.1:7860`).

## How It Works

1. The user inputs a query through the Gradio interface.
2. The query is processed by the Langchain agent, which decides whether to use ArXiv or Wikipedia based on the nature of the question.
3. The agent retrieves relevant information from the chosen source.
4. The Mixtral-8x7b-32768 model generates a response based on the retrieved information and conversation history.
5. The response is displayed to the user through the Gradio interface.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
