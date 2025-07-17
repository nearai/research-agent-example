import asyncio
import os
from typing import Dict

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from gpt_researcher import GPTResearcher
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Research Agent API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


class ResearchRequest(BaseModel):
    query: str
    report_type: str = "research_report"


class ResearchResponse(BaseModel):
    report: str
    sources: list
    costs: dict
    num_sources: int


@app.get("/")
async def root():
    """Serve the main HTML page"""
    return FileResponse("static/index.html")


@app.post("/research", response_model=ResearchResponse)
async def conduct_research(request: ResearchRequest) -> Dict:
    """
    Conduct research using GPT Researcher
    """
    try:
        # Validate API keys
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        if not os.getenv("TAVILY_API_KEY"):
            raise HTTPException(status_code=500, detail="Tavily API key not configured")

        # Create researcher instance
        researcher = GPTResearcher(
            query=request.query, report_type=request.report_type, verbose=True
        )

        # Conduct research
        print(f"Starting research for: {request.query}")
        await researcher.conduct_research()

        # Generate report
        print("Generating report...")
        report = await researcher.write_report()

        # Get additional information
        sources = researcher.get_source_urls()
        costs_value = researcher.get_costs()
        research_sources = researcher.get_research_sources()

        # Format costs as a dictionary
        costs_dict = {
            "total_cost": costs_value if isinstance(costs_value, (int, float)) else 0,
            "total_tokens": 0,  # GPT Researcher doesn't provide token count directly
        }

        return {
            "report": report,
            "sources": sources,
            "costs": costs_dict,
            "num_sources": len(research_sources),
        }

    except Exception as e:
        print(f"Error during research: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "api_keys_configured": {
            "openai": bool(os.getenv("OPENAI_API_KEY")),
            "tavily": bool(os.getenv("TAVILY_API_KEY")),
        },
    }


if __name__ == "__main__":
    import uvicorn

    print("Starting Research Agent Server...")
    print(
        "Make sure you have set OPENAI_API_KEY and TAVILY_API_KEY in your environment"
    )
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
