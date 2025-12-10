# LangChain Chatbot with Local LLM (Ollama)

A chatbot application built with LangChain and Streamlit, powered by a locally running LLM using Ollama. Features LangSmith integration for observability and tracing.

## Features

- 🤖 **Local LLM** - Runs entirely on your machine using Ollama (DeepSeek-R1:1.5B)
- 🔗 **LangChain** - Uses LangChain for prompt templating and chain orchestration
- 🖥️ **Streamlit UI** - Simple and interactive web interface
- 📊 **LangSmith Integration** - Full observability and tracing for your LLM applications
- 🔒 **Privacy-Focused** - No data sent to external APIs (except LangSmith tracing)

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) installed and running
- LangSmith API Key (for tracing)

## Installation

1. **Install Ollama:**
   
   Follow the instructions at [ollama.ai](https://ollama.ai/) to install Ollama for your OS.

2. **Pull the DeepSeek model:**
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

3. **Navigate to the project directory:**
   ```bash
   cd chatbot-local-llm
   ```

4. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set up environment variables:**
   
   Create a `.env` file in the `chatbot-local-llm` directory:
   ```env
   LOCAL_LLM=deepseek-r1:1.5b
   LANGCHAIN_API_KEY=your_langsmith_api_key_here
   ```

## Running the Application

1. **Make sure Ollama is running:**
   ```bash
   ollama serve
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`.

---

## LangSmith Integration

This project uses **LangSmith** for monitoring and debugging your LLM applications.

### What is LangSmith?

[LangSmith](https://smith.langchain.com/) is a platform developed by LangChain for building production-grade LLM applications. It provides:

- **Tracing** - Track every step of your LLM chain execution
- **Debugging** - Identify issues in prompts, chains, and outputs
- **Monitoring** - Observe performance metrics and latency
- **Evaluation** - Test and evaluate your LLM outputs

### How LangSmith is Configured

In `app.py`, LangSmith tracing is enabled with:

```python
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

### Useful Insights from LangSmith

Once tracing is enabled, you can view the following in the [LangSmith Dashboard](https://smith.langchain.com/):

| Feature | Description |
|---------|-------------|
| **Run Traces** | View the complete execution flow of each chain invocation |
| **Input/Output Logs** | See exact prompts sent to the LLM and responses received |
| **Latency Metrics** | Monitor response times for your local LLM |
| **Token Usage** | Track token consumption per request |
| **Error Tracking** | Identify and debug failed runs with detailed error logs |
| **Chain Visualization** | Visualize how prompts, LLMs, and parsers are connected |

### Accessing LangSmith Dashboard

1. Go to [smith.langchain.com](https://smith.langchain.com/)
2. Sign in with your account
3. Navigate to your project to view traces
4. Click on individual runs to see detailed execution logs

### Optional: Set a Project Name

Add this to your `.env` to organize traces by project:

```env
LANGCHAIN_PROJECT=chatbot-local-llm
```

---

## Using Different Local Models

You can use any model available in Ollama. Update the `LOCAL_LLM` in your `.env` file:

```env
# Examples of other models
LOCAL_LLM=llama3.2
LOCAL_LLM=mistral
LOCAL_LLM=codellama
LOCAL_LLM=phi3
```

To see available models:
```bash
ollama list
```

To pull a new model:
```bash
ollama pull <model-name>
```

---

## Project Structure

```
chatbot-local-llm/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .env                # Environment variables (create this)
```

## Tech Stack

- **LangChain** - LLM application framework
- **LangChain Community** - Ollama integration
- **Ollama** - Local LLM runner
- **DeepSeek-R1** - Local language model
- **Streamlit** - Web UI framework
- **LangSmith** - Observability platform
- **python-dotenv** - Environment variable management

## Troubleshooting

### Ollama not running
```bash
# Start Ollama service
ollama serve
```

### Model not found
```bash
# Pull the model first
ollama pull deepseek-r1:1.5b
```

### Slow responses
- Local LLMs depend on your hardware (CPU/GPU)
- Consider using smaller models like `phi3` for faster responses
- Ensure no other heavy processes are running

## License

MIT License
