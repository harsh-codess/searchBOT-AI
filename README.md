# 🔎 LangChain Search Engine Chat

A Streamlit-based chatbot that can search the web using multiple sources including Arxiv, Wikipedia, and DuckDuckGo. Built with LangChain and powered by Groq's Llama3 model.

## Features

- **Multi-source Search**: Integrates Arxiv, Wikipedia, and DuckDuckGo search
- **Real-time Chat**: Interactive chat interface with streaming responses
- **Agent-based Architecture**: Uses LangChain agents for intelligent query handling
- **Streamlit UI**: Clean and intuitive web interface

## Prerequisites

- Python 3.8 or higher
- Groq API Key (get it from [Groq Console](https://console.groq.com/))

## Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "search engine GEN AI"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run "5-Search Engine/app.py"
   ```

## Deployment on Streamlit Cloud

### Step 1: Prepare Your Repository
1. Push your code to GitHub/GitLab/Bitbucket
2. Ensure `.gitignore` excludes `.env` file
3. Make sure `requirements.txt` is in the root directory

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set the main file path: `5-Search Engine/app.py`
6. Click "Deploy"

### Step 3: Configure Secrets
1. In Streamlit Cloud dashboard, go to your app settings
2. Navigate to "Secrets" section
3. Add your environment variables:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

## Alternative Deployment Options

### Heroku
1. Create a `Procfile`:
   ```
   web: streamlit run "5-Search Engine/app.py" --server.port=$PORT --server.address=0.0.0.0
   ```
2. Deploy using Heroku CLI or GitHub integration

### Docker
1. Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "5-Search Engine/app.py"]
   ```

## Usage

1. Enter your Groq API key in the sidebar
2. Start chatting with questions like:
   - "What is machine learning?"
   - "Latest research on quantum computing"
   - "Tell me about climate change"

## Project Structure

```
search engine GEN AI/
├── 5-Search Engine/
│   └── app.py              # Main application
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── .env                   # Environment variables (not in repo)
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
