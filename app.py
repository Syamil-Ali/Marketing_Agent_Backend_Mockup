from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
import httpx

# ----------- INPUT SCHEMA -----------
class MarketInput(BaseModel):
    project_title: str
    product_or_service: str
    business_description: str
    marketing_channels: str
    target_audience: str
    primary_goal: str

# ----------- OUTPUT SCHEMA -----------
class MarketOutput(BaseModel):
    executive_summary: str
    competitors: List[Dict[str, str]]
    market_trends: List[Dict[str, str]]
    audience_insights: List[str]
    pricing_models: List[str]
    opportunities: List[Dict[str, Any]]
    sources: List[str]

app = FastAPI(title="Marketing Strategy Scraper API")

LLM_API_URL = "http://your-llm-model-endpoint"  # Replace with your endpoint

@app.post("/analyze", response_model=MarketOutput)
async def analyze_market(input_data: MarketInput):
    # Static mocked output for testing your model structure without calling external LLM
    mocked_result = {
        "executive_summary": "CloudFlow, an AI-driven SaaS tool focused on workflow optimization for mid-sized tech companies, faces a market with competitors exhibiting weaknesses in customization, integration, and pricing transparency. Key opportunities lie in offering seamless integrations, transparent pricing, and robust AI-driven insights.",
        "competitors": [
            {"name": "Kissflow", "strength": "Low-code/no-code approach", "weakness": "Limited customization and integration issues."},
            {"name": "Nintex", "strength": "Widely adopted", "weakness": "High cost and steep learning curve."},
            {"name": "VegamAI", "strength": "No-code workflow designer", "weakness": "Limited market presence."}
        ],
        "market_trends": [
            {"trend": "AI & ML in workflow automation", "velocity": "accelerating"},
            {"trend": "Demand for no-code/low-code tools", "velocity": "stable"},
            {"trend": "Seamless system integrations", "velocity": "accelerating"},
            {"trend": "Transparent SaaS pricing", "velocity": "accelerating"}
        ],
        "audience_insights": [
            "Tech teams struggle with siloed strategies and inefficient tools.",
            "Resistance to change slows adoption of workflow automation.",
            "High concern around data privacy & compliance.",
            "Integration problems reduce productivity and increase manual work."
        ],
        "pricing_models": [
            "Tiered pricing", "Per-user pricing", "Usage-based add-ons", "Hybrid subscription + usage model"
        ],
        "opportunities": [
            {"opportunity": "Provide advanced customization for complex workflows", "impact_score": 0.9, "confidence": 0.9},
            {"opportunity": "Offer seamless integrations with third-party tools", "impact_score": 0.85, "confidence": 0.9},
            {"opportunity": "Transparent scalable pricing", "impact_score": 0.8, "confidence": 0.85},
            {"opportunity": "Improve user onboarding & reduce learning curve", "impact_score": 0.75, "confidence": 0.8},
            {"opportunity": "Use AI to automate tasks & deliver insights", "impact_score": 0.8, "confidence": 0.75},
            {"opportunity": "Adopt alternative data collection beyond surveys", "impact_score": 0.85, "confidence": 0.8}
        ],
        "sources": [
            "https://www.cloudeagle.ai/blogs/top-kissflow-alternatives-for-workflow-automation",
            "https://www.flowforma.com/blog/nintex-competitors-and-alternatives",
            "https://multishoring.com/blog/challenges-in-implementing-workflow-automation/",
            "https://www.vegam.ai/business-process-automation/tools-comparison",
            "https://www.zluri.com/blog/kissflow-alternatives",
            "https://whatfix.com/blog/digital-transformation-challenges/",
            "https://online.hbs.edu/blog/post/data-collection-methods",
            "https://www.moesif.com/blog/technical/api-development/SaaS-Pricing-Models/"
        ]
    }

    return MarketOutput(**mocked_result)


# ----------- LOCAL DEV MODE -----------
#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

