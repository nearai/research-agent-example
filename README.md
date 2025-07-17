# Research Agent Example

A simple research agent built with [GPT Researcher](https://github.com/assafelovic/gpt-researcher) that provides comprehensive research reports through an easy-to-use web interface.

## Features

- 🔍 **Automated Research**: Conducts thorough research on any topic using multiple web sources
- 📝 **Multiple Report Types**: Generate research reports, resource lists, or outlines
- 🌐 **Web Interface**: Simple, clean HTML interface with no dependencies
- ⚡ **Fast Results**: Get comprehensive reports in minutes
- 📊 **Source Tracking**: See all sources used and research costs
- 🚀 **Easy Setup**: Minimal configuration required

## Prerequisites

- Python 3.11 or later
- OpenAI API key
- Tavily API key (for web search)

## Quick Start

### 1. Clone and Install

```bash
# Clone the repository
git clone <your-repo-url>
cd research-agent-example

# Install dependencies
pip install -r requirements.txt
```

### 2. Set Up API Keys

You need two API keys:

1. **OpenAI API Key**: Get from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **Tavily API Key**: Get from [https://tavily.com/](https://tavily.com/) (free tier available)

Set them as environment variables:

```bash
# Option 1: Export in terminal
export OPENAI_API_KEY="your_openai_api_key_here"
export TAVILY_API_KEY="your_tavily_api_key_here"

# Option 2: Create a .env file
echo "OPENAI_API_KEY=your_openai_api_key_here" >> .env
echo "TAVILY_API_KEY=your_tavily_api_key_here" >> .env
```

### 3. Run the Server

```bash
python server.py
```

The server will start at `http://localhost:8000`

## Usage

1. Open your browser and go to `http://localhost:8000`
2. Enter your research query (e.g., "Latest developments in quantum computing")
3. Select the report type:
   - **Research Report**: Comprehensive analysis with citations
   - **Resource Report**: List of relevant resources and links
   - **Outline Report**: Structured outline for the topic
4. Click "Start Research" and wait for results

## Project Structure

```
research-agent-example/
├── server.py              # FastAPI backend server
├── static/
│   └── index.html        # Web interface
├── requirements.txt      # Python dependencies
├── env_setup.txt        # Environment setup guide
└── README.md            # This file
```

## API Endpoints

- `GET /` - Serves the web interface
- `POST /research` - Conducts research and returns report
- `GET /health` - Health check and API key status

### Research Endpoint

```bash
curl -X POST "http://localhost:8000/research" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the latest AI trends?",
    "report_type": "research_report"
  }'
```

Response:
```json
{
  "report": "# Research Report\n\n...",
  "sources": ["https://...", "https://..."],
  "costs": {
    "total_cost": 0.1234,
    "total_tokens": 5678
  },
  "num_sources": 15
}
```

## Configuration

The research agent uses GPT-4 models by default. Average research:
- Takes ~3 minutes to complete
- Costs ~$0.10 per research task
- Analyzes 20+ web sources

## Troubleshooting

### "API keys not configured" warning
- Ensure both `OPENAI_API_KEY` and `TAVILY_API_KEY` are set
- Check the `/health` endpoint to verify configuration

### Research takes too long
- Complex topics may take 3-5 minutes
- The agent is gathering information from multiple sources

### Empty or short reports
- Ensure your query is specific enough
- Try using "Research Report" type for comprehensive results

## Security Notes

- Never commit API keys to version control
- Add `.env` to your `.gitignore` file
- Use environment variables or secure key management in production

## Learn More

- [GPT Researcher Documentation](https://docs.gptr.dev/)
- [GPT Researcher GitHub](https://github.com/assafelovic/gpt-researcher)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Tavily API Documentation](https://docs.tavily.com/)

## License

This example is provided as-is for educational purposes. 
