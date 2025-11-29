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


class MarketingStrategyOutput(BaseModel):
    diagnosis: str
    strategic_direction: str
    strategy_pillars: List[str]
    messaging_framework: Dict[str, List[str]]
    go_to_market_plan: Dict[str, List[str]]
    priorities: List[str]

class ContentStrategyOutput(BaseModel):
    core_message: str
    content_goals: List[str]
    audience_motivations: List[str]
    strategic_angles: List[str]
    recommended_formats: List[str]
    channel_playbook: Dict[str, List[str]]
    mandatory_inclusions: Dict[str, List[str]]

# ----------- COMBINED OUTPUT -----------
class StrategicOutput(BaseModel):
    market_analysis: MarketOutput
    marketing_strategy: MarketingStrategyOutput
    content_strategy: ContentStrategyOutput

# ------------------------------------------

app = FastAPI(title="Marketing Strategy Scraper API")

LLM_API_URL = "http://your-llm-model-endpoint"  # Replace with your endpoint

@app.post("/analyze", response_model=MarketOutput)
async def market_analysis(input_data: MarketInput):
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



# ----------- ENDPOINT 2: STRATEGIC ANALYSIS (MARKETING STRATEGY + MARKET) -----------
@app.post("/strategic-analysis", response_model=StrategicOutput)
async def strategic_analysis(input_data: MarketInput):
    # Reuse mocked market analysis
    market_analysis_result = await market_analysis(input_data)
    
    marketing_strategy_result = {
        "diagnosis": "Mid-sized tech companies struggle with workflow inefficiencies due to siloed strategies, software sprawl, employee resistance, and data privacy concerns. Existing workflow automation tools often fall short, with limitations in customization, integration, pricing transparency, and user experience. This creates an opportunity for an AI-driven solution that addresses these gaps by providing seamless integrations, transparent pricing, intuitive design, and robust AI insights, leveraging alternative data collection methods for deeper, more accurate workflow analysis.",
        "strategic_direction": "CloudFlow should win by offering mid-sized tech companies an AI-powered workflow automation solution that delivers highly customizable, easily integrated, and transparently priced insights, driving demonstrable improvements in team efficiency and data-driven decision-making.",
        "strategy_pillars": [
            "AI-Powered Insights: Leverage real-time behavioral data and machine learning to provide uniquely accurate, actionable recommendations for workflow optimization, surpassing the limitations of traditional survey-based methods.",
            "Seamless Integration & Customization: Offer extensive integration capabilities with existing systems and advanced customization options to address complex workflows, overcoming the integration challenges and limited customization of competitors like Kissflow and Nintex.",
            "Transparent & Flexible Pricing: Implement transparent and scalable pricing plans, including tiered and usage-based options, to alleviate concerns about rising costs and provide predictable value as organizations grow, directly addressing a key market pain point."
        ],
        "messaging_framework": {
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
        },
        "go_to_market_plan": {
            "channels": [
                "LinkedIn (Targeted ads to tech companies and HR departments)",
                "SaaS industry blogs and publications",
                "Webinars and online events showcasing AI-driven workflow automation",
                "Partnerships with complementary SaaS providers"
            ],
            "plays": [
                "Freemium model with tiered feature access",
                "Targeted content marketing showcasing ROI of AI-driven workflow improvements",
                "Case studies highlighting successful integrations and customizations",
                "Interactive demos and free trials emphasizing ease of use and data privacy"
            ],
            "motion": [
                "PLG (Product-Led Growth) with self-serve onboarding and in-app support, augmented by sales-assisted upgrades for larger accounts."
            ]
        },
        "priorities": [
            "Develop and launch the core AI-powered workflow analysis engine.",
            "Build seamless integrations with popular SaaS tools used by mid-sized tech companies.",
            "Implement transparent and flexible pricing plans.",
            "Create targeted content marketing materials showcasing the value of CloudFlow.",
            "Establish partnerships with complementary SaaS providers."
        ]
    }

    content_strategy_result = {
        "core_message": (
            "CloudFlow unlocks peak team performance in mid-sized tech companies "
            "by providing uniquely accurate, AI-powered insights and customizable "
            "automation that legacy tools miss."
        ),
        "content_goals": [
            "Generate awareness of CloudFlow's unique AI-driven approach to workflow optimization.",
            "Build trust by demonstrating the accuracy and reliability of CloudFlow's insights.",
            "Drive engagement through interactive demos and valuable content showcasing workflow improvements.",
            "Educate the audience on real-time behavioral data vs. traditional surveys.",
            "Facilitate sign-ups through freemium and targeted content.",
            "Address data privacy concerns by highlighting security and compliance measures."
        ],
        "audience_motivations": [
            "Increase team efficiency",
            "Reduce bottlenecks",
            "Improve decision-making",
            "Find scalable solutions",
            "Integrate easily with existing systems",
            "Ensure data privacy"
        ],
        "strategic_angles": [
            "The Hidden Costs of Inefficient Workflows",
            "Beyond Surveys: Real Behavioral Insight",
            "AI-Powered Workflow Automation for Mid-Sized Tech",
            "Seamless Integration, Zero Disruption",
            "From Insight to Action: Real-World Transformations"
        ],
        "recommended_formats": [
            "Webinars", "Case Studies", "Blog Posts", "Infographics",
            "Product Demos", "Whitepapers", "LinkedIn Articles", "Short Videos"
        ],
        "channel_playbook": {
            "LinkedIn": [
                "Targeted ads to HR & operations leaders.",
                "Thought leadership on workflow automation.",
                "Sponsored success-story content."
            ],
            "SaaS Blogs and Publications": [
                "Guest posts",
                "Industry commentary",
                "Product review placements"
            ],
            "Webinars and Online Events": [
                "AI workflow automation webinars",
                "Product demos & Q&A sessions"
            ],
            "Partnerships with SaaS Providers": [
                "Co-marketing efforts",
                "Bundled workflows",
                "Joint messaging campaigns"
            ]
        },
        "mandatory_inclusions": {
            "value_prop": [
                "CloudFlow: Unlock peak team performance with AI-powered workflow automation."
            ],
            "key_messages": [
                "Eliminate workflow bottlenecks with AI insights.",
                "Customize and integrate effortlessly.",
                "Predictable value with transparent pricing.",
                "Secure and compliant workflow data analysis."
            ],
            "proof_points": [
                "10x more accurate insights than surveys.",
                "Advanced workflow customization.",
                "Wide third-party integration support.",
                "Transparent and scalable pricing."
            ]
        }
    }
    
    return StrategicOutput(
        market_analysis=market_analysis_result,
        marketing_strategy=MarketingStrategyOutput(**marketing_strategy_result),
        content_strategy=ContentStrategyOutput(**content_strategy_result)
        
    )
# ----------- LOCAL DEV MODE -----------
#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



