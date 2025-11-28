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


class ContentStrategyOutput(BaseModel):
    core_message: str
    content_goals: List[str]
    audience_motivations: List[str]
    strategic_angles: List[str]
    recommended_formats: List[str]
    channel_playbook: Dict[str, List[str]]
    mandatory_inclusions: Dict[str, List[str]]

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


@app.post("/content-strategy", response_model=ContentStrategyOutput)
async def content_strategy(input_data: MarketInput):
    content_strategy_result = {
        "core_message": "CloudFlow unlocks peak team performance in mid-sized tech companies by providing uniquely accurate, AI-powered insights and customizable automation that legacy tools miss.",
        "content_goals": [
            "Generate awareness of CloudFlow's unique AI-driven approach to workflow optimization.",
            "Build trust by demonstrating the accuracy and reliability of CloudFlow's insights.",
            "Drive engagement through interactive demos and valuable content showcasing workflow improvements.",
            "Educate the audience on the benefits of real-time behavioral data analysis vs. traditional surveys.",
            "Facilitate sign-ups and conversions through a freemium model and targeted content.",
            "Address data privacy concerns by highlighting security and compliance measures."
        ],
        "audience_motivations": [
            "Increase team efficiency and productivity.",
            "Reduce workflow bottlenecks and friction.",
            "Improve data-driven decision-making.",
            "Find affordable and scalable solutions.",
            "Seamlessly integrate new tools with existing systems.",
            "Ensure data privacy and security."
        ],
        "strategic_angles": [
            "The Hidden Costs of Inefficient Workflows: Quantify the financial impact of workflow bottlenecks and highlight how CloudFlow provides a clear ROI.",
            "Beyond Surveys: Uncover the Truth About Your Team's Workflow: Focus on the limitations of traditional survey data and the superiority of real-time behavioral analysis.",
            "AI-Powered Workflow Automation for Mid-Sized Tech: Tailor the message to the unique challenges and opportunities of mid-sized tech companies, emphasizing scalability and customization.",
            "Seamless Integration, Zero Disruption: Showcase the ease of integrating CloudFlow with existing tools and the minimal disruption to existing workflows.",
            "From Insight to Action: Real-World Workflow Transformations: Present case studies and examples of how CloudFlow has helped companies like theirs achieve tangible results."
        ],
        "recommended_formats": ["Webinars", "Case Studies", "Blog Posts", "Infographics", "Product Demos", "Whitepapers", "LinkedIn Articles", "Short Videos"],
        "channel_playbook": {
            "LinkedIn": [
                "Targeted ads to HR, operations, and tech decision-makers in mid-sized tech companies.",
                "Share valuable content and thought leadership articles on AI-driven workflow automation.",
                "Run sponsored content highlighting customer success stories and product demos."
            ],
            "SaaS Blogs and Publications": [
                "Publish guest posts and articles on workflow optimization and the benefits of AI.",
                "Participate in industry discussions and forums.",
                "Secure product reviews and comparisons."
            ],
            "Webinars and Online Events": [
                "Host webinars showcasing AI-driven workflow automation.",
                "Offer interactive product demos and Q&A sessions.",
                "Partner with industry experts and thought leaders."
            ],
            "Partnerships with SaaS Providers": [
                "Co-market CloudFlow with complementary SaaS tools.",
                "Offer bundled solutions and integrated workflows.",
                "Cross-promote each other's products to relevant customer segments."
            ]
        },
        "mandatory_inclusions": {
            "value_prop": ["CloudFlow: Unlock peak team performance with AI-powered workflow automation. Get 10x more accurate insights and fix friction points others miss."],
            "key_messages": [
                "Eliminate workflow bottlenecks with AI-driven insights tailored to your team's actual behavior.",
                "Seamlessly integrate with your existing tools and customize workflows to fit your unique needs.",
                "Gain clear, predictable value with our transparent and scalable pricing plans.",
                "Address data privacy concerns with our secure and compliant AI-driven workflow analysis."
            ],
            "proof_points": [
                "AI-powered analysis of real-time behavioral data, providing 10x more accurate insights compared to traditional surveys.",
                "Advanced customization options to handle complex workflows, differentiating from competitors with limited customization.",
                "Seamless integration with a wide array of third-party applications, avoiding integration challenges faced by competitors.",
                "Transparent and scalable pricing plans to address concerns about rising costs as organizations grow."
            ]
        }
    }
    return ContentStrategyOutput(**content_strategy_result)

# ----------- LOCAL DEV MODE -----------
#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
