from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
import httpx




class MarketResearchRequest(BaseModel):
    project_brief: Dict[str, Any]
    max_urls_per_query: int = 2
    max_urls_total: Optional[int] = None


class MarketResearchOutput(BaseModel):
    project_brief: Dict[str, Any]
    compiled_summaries: Dict[str, Any]
    market_research: Dict[str, Any]

class StrategyRequest(BaseModel):
    project_brief: Dict[str, Any]
    market_result: Optional[Dict[str, Any]] = None
    require_exploration: bool = False
    max_urls_per_query: int = 2
    max_urls_total: Optional[int] = None

# ----------- INPUT SCHEMA -----------
class MarketInput(BaseModel):
    project_title: str
    product_or_service: str
    business_description: str
    marketing_channels: str
    target_audience: str
    primary_goal: str


class ContentStrategyInput(BaseModel):
    core_message: str
    content_goals: str
    audience_motivations: str
    strategic_angles: str
    key_messages: str
    tone_and_voice: str
    requested_format: str


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


class ContentBriefOutput(BaseModel):
    brief_title: str
    core_message: str
    creative_angles: List[str]
    content_goals: List[str]
    audience_profile: str
    mandatory_inclusions: Dict[str, List[str]]
    recommended_formats: List[str]
    channel_guidance: Dict[str, List[str]]
    tone_and_voice: str
    constraints: List[str]

class ContentCreationOutput(BaseModel):
    final_content: str
    applied_angles: List[str]
    key_inclusions: Dict[str, List[str]]
    tone_and_voice: str
    format: str

# ----------- COMBINED OUTPUT -----------
class StrategicOutput(BaseModel):
    market_analysis: MarketOutput
    marketing_strategy: MarketingStrategyOutput
    content_strategy: ContentStrategyOutput

class ContentCreationInput(BaseModel):
    market: MarketInput
    strategy: ContentStrategyInput

class FullContentCreationResponse(BaseModel):
    brief: ContentBriefOutput
    content: ContentCreationOutput

# ------------------------------------------

app = FastAPI(title="Marketing Strategy Scraper API")

LLM_API_URL = "http://your-llm-model-endpoint"  # Replace with your endpoint

@app.post("/analyze", response_model=MarketResearchOutput)
async def market_analysis(input_data: MarketResearchRequest):
    # Static mocked output for testing your model structure without calling external LLM
    mocked_result = {
           "project_brief":{
              "request_type":"STRATEGY",
              "project_title":"SaaS Product Marketing Strategy",
              "product_or_service":"Koboi AI",
              "business_description":"Koboi AI is the All-in-One AI Marketing Strategist for forward-thinking businesses. We automate the entire marketing process, from deep-web research and competitive analysis to generating a complete, tailored strategy and high-impact content. Stop guessing and start converting.",
              "marketing_channels":"None",
              "content_format":"None",
              "goals":"Acquire 100 users in the first 3 months",
              "target_audience":"Forward-thinking businesses",
              "missing_information":[
                 
              ]
           },
           "compiled_summaries":{
              "Top AI marketing strategy software weaknesses":{
                 "https://storyteq.com/blog/what-are-the-limitations-of-ai-in-marketing-technology/":{
                    "relevance":0.9,
                    "impact_score":0.8,
                    "summary":"AI in marketing technology has limitations in contextual understanding, creativity, and ethics. It relies on high-quality data and struggles with brand nuance and emotional storytelling. Human oversight is essential for strategy, creative direction, and ethical considerations to ensure brand consistency and prevent generic content.",
                    "key_points":[
                       "AI requires vast amounts of high-quality data to function effectively.",
                       "AI struggles with understanding brand context and nuance, leading to generic content.",
                       "Human creativity outperforms AI in original concept development and emotional storytelling.",
                       "Ethical limitations of AI include privacy concerns, bias reinforcement, and lack of moral reasoning.",
                       "An effective balance between AI and human input involves using AI for data analysis and optimization, while humans control creative direction and ethical decisions."
                    ],
                    "strategic_insights":[
                       "Koboi AI needs to focus on areas where AI excels, such as data analysis and content variation, while ensuring human oversight for creative and strategic decisions.",
                       "Differentiate Koboi AI by addressing the ethical concerns surrounding AI, such as data privacy and bias, by implementing robust security measures and ethical guidelines.",
                       "Highlight the importance of human creativity and emotional intelligence in marketing, positioning Koboi AI as a tool that enhances rather than replaces human input."
                    ]
                 }
              },
              "AI marketing platform features underserved business needs":{
                 "https://www.mdpi.com/2071-1050/17/20/9336":{
                    "relevance":0.9,
                    "impact_score":0.85,
                    "summary":"This research investigates how AI-powered advisory platforms can address underserved business needs, specifically for SMEs in the U.S. The study found that integrated platforms offering multiple modules (MarketRadar, StrategicCoaching, ComplianceAlerts, PeerBenchmarking) drive better marketing outcomes than standalone tools. These findings emphasize the importance of modular AI design for improving marketing decision-making in capital-constrained SMEs.",
                    "key_points":[
                       "SMEs in underserved U.S. markets face barriers adopting AI for digital marketing.",
                       "An AI-driven unified advisory platform was tested, integrating market insights, coaching, and compliance tools.",
                       "SMEs using multiple modules of the platform achieved higher customer acquisition and revenue.",
                       "Trust elements like PeerBenchmarks and ComplianceAlerts are key for platform adoption.",
                       "The study introduces the 'compound benefits' framework to explain synergistic performance outcomes from cross-module AI engagement."
                    ],
                    "strategic_insights":[
                       "Koboi AI can differentiate by offering modular and integrated AI marketing tools tailored to SMEs.",
                       "Focus on building trust through transparency and explainability in AI recommendations.",
                       "Partnerships with CDFIs and local incubators can facilitate adoption in underserved markets.",
                       "Address digital literacy gaps with targeted training and user-friendly interfaces.",
                       "Prioritize ethical considerations, such as bias mitigation, in AI design and implementation."
                    ]
                 }
              },
              "Pricing model gaps in AI marketing automation software 2025":{
                 "https://digitalagencynetwork.com/ai-agency-pricing/":{
                    "relevance":0.9,
                    "impact_score":0.9,
                    "summary":"The AI Agency Pricing Guide 2025 indicates that AI marketing automation pricing models are shifting from flat retainers and hourly rates to hybrid, performance-based, and usage-driven models. There's a wide range, from $99/month automation packages to $500K+ custom AI builds. Pricing transparency is increasing, with agencies separating platform costs (like OpenAI token usage) from execution fees.",
                    "key_points":[
                       "AI SEO services average $3,200/month, with retainers ranging from $2,000 to $20,000+.",
                       "Custom AI development projects span $50K to $500K+, while SaaS-style offerings start at $99/month.",
                       "AI automation builds typically cost $2,500 to $15,000+, with ongoing monitoring retainers from $500 to $5,000+.",
                       "OpenAI’s GPT‑4 Turbo pricing ranges from $0.003 to $0.012 per 1,000 tokens, depending on usage tier."
                    ],
                    "strategic_insights":[
                       "Koboi AI can explore hybrid pricing models (retainer + usage-based) to balance predictable revenue with value-based pricing.",
                       "There's an opportunity to offer tiered pricing for different levels of AI marketing automation, from basic automation to advanced personalization and analytics.",
                       "Koboi AI should consider offering productized services (e.g., AI content generation packages) to scale more predictably compared to custom AI projects.",
                       "Focus on transparent pricing by clearly separating platform costs from service fees to build trust with forward-thinking businesses."
                    ]
                 }
              },
              "Leading AI marketing strategy brands user reviews and complaints":{
                 "https://www.m1-project.com/blog/best-20-ai-marketing-use-cases#:~:text=Amazon%2C%20HubSpot%2C%20and%20Meta%20use,models%20that%20predict%20user%20behavior.":{
                    "relevance":0.8,
                    "impact_score":0.7,
                    "summary":"M1-Project's blog post discusses 20 AI marketing use cases, emphasizing how AI can transform marketing by reducing costs, increasing conversions, and scaling marketing efforts. It highlights the importance of an adaptive AI orchestration framework and provides practical examples of how AI can be used to improve various marketing functions. It is important to note that the platform M1-Project offers a suite of tools, like the 'Marketing Strategy Builder', that aims to provide forward-thinking businesses with an All-in-One AI Marketing Strategist.",
                    "key_points":[
                       "AI can reduce customer acquisition costs and increase ROI through automated data analysis and personalization.",
                       "An adaptive AI orchestration framework can significantly boost digital conversions.",
                       "AI can be used for customer segmentation, predictive analytics, automated content creation, and campaign planning.",
                       "M1-project's tools like ICP Generator, Marketing Strategy Builder, and Social Media Content Generator can be integrated into an AI framework."
                    ],
                    "strategic_insights":[
                       "Koboi AI can leverage similar AI-driven strategies to automate and optimize marketing processes, potentially offering a competitive advantage.",
                       "Focusing on emotion AI and real-time adaptation could differentiate Koboi AI from competitors.",
                       "Highlighting use cases with quantifiable results (e.g., increased conversions, reduced costs) in marketing materials can attract forward-thinking businesses."
                    ]
                 }
              },
              "Whitespace opportunities in AI powered marketing solutions":{
                 "https://www.demandfarm.com/blog/unlocking-white-space-opportunities-using-ai/":{
                    "relevance":0.9,
                    "impact_score":0.85,
                    "summary":"DemandFarm emphasizes leveraging AI-powered analytics to identify white space opportunities within key account management. They highlight the use of AI in understanding customer intent, optimizing touchpoints, personalizing content, and hyper-targeting messaging to improve sales and marketing strategies. Social analytics is also presented as a method for identifying unexplored market segments and understanding competitor strategies.",
                    "key_points":[
                       "AI can assist in identifying account intent and optimizing customer touchpoints.",
                       "Personalized content and hyper-targeted messaging, driven by AI, can enhance customer engagement.",
                       "Social analytics helps in discovering unexplored market segments and competitor strategies.",
                       "AI can accelerate white space analysis by providing a clear view of customer investments and helping to shortlist the right accounts for cross-selling."
                    ],
                    "strategic_insights":[
                       "Koboi AI can focus on developing features that provide AI-driven insights into customer intent and behavior, enabling more personalized and effective marketing strategies.",
                       "Opportunity to integrate social analytics capabilities to help businesses identify white space opportunities by monitoring market trends and competitor activities on social media.",
                       "Consider offering AI-powered tools that streamline white space analysis, making it easier for sales teams to identify and capitalize on cross-selling opportunities, contributing to the goal of acquiring 100 users by showcasing the value of AI in uncovering hidden revenue potential."
                    ]
                 }
              }
           },
           "market_research":{
              "executive_summary":"Koboi AI can differentiate itself by offering modular, integrated AI marketing tools tailored to SMEs, focusing on building trust through transparency and explainability in AI recommendations. Hybrid pricing models balancing predictable revenue with value-based pricing, tiered pricing for different levels of AI marketing automation, and productized services can also provide a competitive advantage.",
              "competitors":[
                 {
                    "name":"M1-Project",
                    "description":"Offers a suite of AI-driven marketing tools, including a 'Marketing Strategy Builder'.",
                    "strength":"Provides an all-in-one AI Marketing Strategist.",
                    "weakness":"May lack focus on specific areas like emotion AI and real-time adaptation."
                 },
                 {
                    "name":"HubSpot",
                    "description":"Leading marketing automation platform.",
                    "strength":"Extensive marketing automation capabilities and brand recognition.",
                    "weakness":"Can be complex and expensive for smaller businesses."
                 },
                 {
                    "name":"Meta",
                    "description":"Provides AI-driven advertising and marketing solutions.",
                    "strength":"Massive reach and data for ad targeting.",
                    "weakness":"Raises privacy concerns and can be expensive for smaller campaigns."
                 }
              ],
              "market_trends":[
                 {
                    "trend":"Shift towards hybrid and performance-based pricing models",
                    "velocity":"accelerating"
                 },
                 {
                    "trend":"Importance of modular and integrated AI marketing platforms",
                    "velocity":"stable"
                 },
                 {
                    "trend":"Need for transparency and explainability in AI recommendations",
                    "velocity":"increasing"
                 }
              ],
              "audience_insights":[
                 "SMEs in underserved U.S. markets face barriers adopting AI for digital marketing.",
                 "Forward-thinking businesses seek AI solutions that reduce customer acquisition costs and increase ROI.",
                 "Businesses want to easily identify and capitalize on cross-selling opportunities."
              ],
              "pricing_models":[
                 "Hybrid pricing (retainer + usage-based)",
                 "Tiered pricing for different levels of AI marketing automation",
                 "Productized services (e.g., AI content generation packages)"
              ],
              "opportunities":[
                 {
                    "opportunity":"Offer modular and integrated AI marketing tools tailored to SMEs",
                    "impact_score":0.9,
                    "confidence":0.9
                 },
                 {
                    "opportunity":"Focus on building trust through transparency and explainability in AI recommendations",
                    "impact_score":0.85,
                    "confidence":0.95
                 },
                 {
                    "opportunity":"Integrate social analytics capabilities to help businesses identify white space opportunities",
                    "impact_score":0.8,
                    "confidence":0.85
                 }
              ],
              "sources":[
                 "https://storyteq.com/blog/what-are-the-limitations-of-ai-in-marketing-technology/",
                 "https://www.mdpi.com/2071-1050/17/20/9336",
                 "https://digitalagencynetwork.com/ai-agency-pricing/",
                 "https://www.m1-project.com/blog/best-20-ai-marketing-use-cases#:~:text=Amazon%2C%20HubSpot%2C%20and%20Meta%20use,models%20that%20predict%20user%20behavior.",
                 "https://www.demandfarm.com/blog/unlocking-white-space-opportunities-using-ai/"
              ]
           }
        }
    return mocked_result



# ----------- ENDPOINT 2: STRATEGIC ANALYSIS (MARKETING STRATEGY + MARKET) -----------
@app.post("/strategic-analysis") # response_model=StrategicOutput
async def strategic_analysis(input_data: StrategyRequest):
    # Reuse mocked market analysis
    market_analysis_result = await market_analysis(input_data)
    
    mockup_result = {'marketing_strategy': {'diagnosis': 'SMEs in underserved U.S. markets face significant barriers in adopting AI for digital marketing, despite a growing need for solutions that reduce customer acquisition costs and increase ROI. Competitors like HubSpot and Meta are often too complex or expensive, while others may lack focus. This creates an opportunity for AI solutions tailored to SMEs that easily identify cross-selling opportunities and build trust through transparency.',
      'strategic_direction': 'Koboi AI will win by providing a modular, transparent, and integrated AI marketing platform specifically designed for SMEs in underserved U.S. markets, delivering measurable ROI and actionable insights.',
      'strategy_pillars': ['Modular AI Solutions: Offer a suite of AI tools that can be adopted individually or integrated, catering to the specific needs and budgets of SMEs.',
       "Transparency and Explainability: Focus on building trust by providing clear, understandable AI recommendations and insights, addressing the 'black box' concern.",
       'Actionable ROI: Prioritize features that directly reduce customer acquisition costs, increase ROI, and identify cross-selling opportunities for immediate impact.'],
      'messaging_framework': {'value_prop': ['Koboi AI: Your All-in-One AI Marketing Strategist for forward-thinking businesses. Stop guessing, start converting.'],
       'key_messages': ['Get enterprise-level AI marketing strategy at a small business price.',
        'Finally, AI-driven marketing insights that you can understand and trust.',
        'Reduce customer acquisition costs and maximize ROI with AI-powered cross-selling.'],
       'proof_points': ['AI algorithms analyze deep-web data to identify hidden market opportunities.',
        'Transparency in AI recommendations builds trust and facilitates adoption.',
        'Modular design allows businesses to customize AI tools to their specific needs and budget.']},
      'go_to_market_plan': {'channels': ['Content Marketing (blog, webinars, case studies)',
        'Social Media (LinkedIn, Twitter)',
        'Partnerships with SME-focused organizations',
        'Online advertising (Google Ads, social media ads targeting SMEs)'],
       'plays': ['Free trial with limited features to showcase value',
        'Educational content focused on AI marketing for SMEs',
        "Webinars demonstrating the platform's capabilities",
        'Case studies highlighting successful SME implementations'],
       'motion': ['Self-serve with guided onboarding for initial user acquisition',
        'Sales-assisted for larger or complex SME accounts']},
      'priorities': ['Develop core modular AI marketing tools (strategy builder, content generator).',
       'Implement transparency and explainability features in AI recommendations.',
       "Create content and resources tailored to SMEs' AI marketing needs.",
       'Establish partnerships with SME-focused organizations for distribution.',
       'Offer hybrid and tiered pricing models to increase adoption.']},
     'content_strategy': {'core_message': 'Koboi AI empowers forward-thinking businesses in underserved U.S. markets to achieve measurable ROI through transparent, modular, and integrated AI marketing solutions, eliminating guesswork and driving conversions.',
      'content_goals': ['Awareness of Koboi AI as a tailored solution for SMEs.',
       'Education on the benefits of AI in marketing for SMEs.',
       'Trust-building through transparent AI recommendations.',
       'Engagement with modular AI tools and their specific applications.',
       'Conversion to free trial users and ultimately, paying customers.',
       'Objection-handling related to the complexity and cost of AI solutions.'],
      'audience_motivations': ['Reduce customer acquisition costs.',
       'Increase marketing ROI.',
       'Gain actionable insights without complex analysis.',
       'Implement AI solutions that are easy to understand and trust.',
       'Customize AI tools to their specific business needs and budget.',
       'Identify cross-selling opportunities to maximize revenue.'],
      'strategic_angles': ["Demystifying AI: Koboi AI breaks down the 'black box' of AI, providing transparent and understandable recommendations for SMEs.",
       "Modular AI for Every Need: Showcase how Koboi AI's modular design allows businesses to start small and scale their AI adoption based on specific needs and budget.",
       'ROI-Focused AI: Highlight case studies and data demonstrating how Koboi AI directly reduces customer acquisition costs and increases ROI for SMEs.',
       'AI-Powered Cross-Selling: Focus on how Koboi AI identifies hidden cross-selling opportunities to drive revenue growth.',
       'Leveling the Playing Field: Position Koboi AI as the solution that brings enterprise-level AI marketing strategy to SMEs at an affordable price.'],
      'recommended_formats': ['Blog posts explaining AI concepts and their application to SME marketing.',
       "Webinars demonstrating the platform's capabilities and ROI.",
       'Case studies highlighting successful SME implementations.',
       'Short explainer videos showcasing the transparency and ease of use of Koboi AI.',
       'Interactive ROI calculators allowing SMEs to estimate potential gains.',
       'Social media content sharing tips and insights on AI marketing for SMEs.'],
      'channel_playbook': {'Content Marketing (blog, webinars, case studies)': ['Focus on educational content that addresses the specific AI marketing needs and challenges of SMEs.',
        'Showcase successful SME implementations and ROI achieved through Koboi AI.'],
       'Social Media (LinkedIn, Twitter)': ['Engage with SME communities and share valuable insights on AI marketing.',
        'Promote webinars, case studies, and other educational content.',
        'Highlight the transparency and ease of use of Koboi AI.'],
       'Partnerships with SME-focused organizations': ['Collaborate on webinars and content creation to reach a wider audience.',
        'Offer exclusive discounts or trials to members of partner organizations.',
        'Build trust and credibility through endorsements from trusted SME advocates.'],
       'Online advertising (Google Ads, social media ads targeting SMEs)': ['Target SMEs in underserved U.S. markets with ads highlighting the ROI and affordability of Koboi AI.',
        'Use ad copy that emphasizes the transparency and ease of use of the platform.',
        'Run retargeting campaigns to drive free trial sign-ups.']},
      'mandatory_inclusions': {'value_prop': ['All-in-One AI Marketing Strategist',
        'Stop guessing, start converting',
        'Enterprise-level AI marketing strategy at a small business price'],
       'key_messages': ['AI-driven marketing insights that you can understand and trust.',
        'Reduce customer acquisition costs and maximize ROI with AI-powered cross-selling.',
        'Modular design allows businesses to customize AI tools to their specific needs and budget.'],
       'proof_points': ['AI algorithms analyze deep-web data to identify hidden market opportunities.',
        'Transparency in AI recommendations builds trust and facilitates adoption.',
        'Modular design allows businesses to customize AI tools to their specific needs and budget.',
        'Data-backed ROI improvements for SMEs in underserved markets.']}},
     'market_research': {'executive_summary': 'Koboi AI can differentiate itself by offering modular, integrated AI marketing tools tailored to SMEs, focusing on building trust through transparency and explainability in AI recommendations. Hybrid pricing models balancing predictable revenue with value-based pricing, tiered pricing for different levels of AI marketing automation, and productized services can also provide a competitive advantage.',
      'competitors': [{'name': 'M1-Project',
        'description': "Offers a suite of AI-driven marketing tools, including a 'Marketing Strategy Builder'.",
        'strength': 'Provides an all-in-one AI Marketing Strategist.',
        'weakness': 'May lack focus on specific areas like emotion AI and real-time adaptation.'},
       {'name': 'HubSpot',
        'description': 'Leading marketing automation platform.',
        'strength': 'Extensive marketing automation capabilities and brand recognition.',
        'weakness': 'Can be complex and expensive for smaller businesses.'},
       {'name': 'Meta',
        'description': 'Provides AI-driven advertising and marketing solutions.',
        'strength': 'Massive reach and data for ad targeting.',
        'weakness': 'Raises privacy concerns and can be expensive for smaller campaigns.'}],
      'market_trends': [{'trend': 'Shift towards hybrid and performance-based pricing models',
        'velocity': 'accelerating'},
       {'trend': 'Importance of modular and integrated AI marketing platforms',
        'velocity': 'stable'},
       {'trend': 'Need for transparency and explainability in AI recommendations',
        'velocity': 'increasing'}],
      'audience_insights': ['SMEs in underserved U.S. markets face barriers adopting AI for digital marketing.',
       'Forward-thinking businesses seek AI solutions that reduce customer acquisition costs and increase ROI.',
       'Businesses want to easily identify and capitalize on cross-selling opportunities.'],
      'pricing_models': ['Hybrid pricing (retainer + usage-based)',
       'Tiered pricing for different levels of AI marketing automation',
       'Productized services (e.g., AI content generation packages)'],
      'opportunities': [{'opportunity': 'Offer modular and integrated AI marketing tools tailored to SMEs',
        'impact_score': 0.9,
        'confidence': 0.9},
       {'opportunity': 'Focus on building trust through transparency and explainability in AI recommendations',
        'impact_score': 0.85,
        'confidence': 0.95},
       {'opportunity': 'Integrate social analytics capabilities to help businesses identify white space opportunities',
        'impact_score': 0.8,
        'confidence': 0.85}],
      'sources': ['https://storyteq.com/blog/what-are-the-limitations-of-ai-in-marketing-technology/',
       'https://www.mdpi.com/2071-1050/17/20/9336',
       'https://digitalagencynetwork.com/ai-agency-pricing/',
       'https://www.m1-project.com/blog/best-20-ai-marketing-use-cases#:~:text=Amazon%2C%20HubSpot%2C%20and%20Meta%20use,models%20that%20predict%20user%20behavior.',
       'https://www.demandfarm.com/blog/unlocking-white-space-opportunities-using-ai/']}}
    
    
    return mockup_result




@app.post("/content-creation", response_model=FullContentCreationResponse)
def create_content(input: ContentCreationInput):

    # ----- 1. Content Brief -----
    brief = ContentBriefOutput(
        brief_title="CloudFlow B2B SaaS Launch: AI-Powered Workflow Optimization for Tech Companies",
        core_message="CloudFlow unlocks peak team performance in mid-sized tech companies with uniquely accurate, AI-powered insights and customizable automation that legacy tools miss.",
        creative_angles=[
            "Quantify the hidden financial costs of inefficient workflows and highlight CloudFlow's ROI.",
            "Showcase the limitations of traditional surveys and the superior accuracy of CloudFlow's real-time behavioral analysis.",
            "Tailor messaging to the unique challenges of mid-sized tech, emphasizing scalability and customization.",
            "Demonstrate seamless integration with existing tools for zero disruption.",
            "Present case studies illustrating tangible workflow transformations achieved with CloudFlow."
        ],
        content_goals=[
            "Generate awareness of CloudFlow's unique AI-driven approach.",
            "Build trust by demonstrating the accuracy of insights.",
            "Drive engagement through interactive demos.",
            "Educate on the benefits of real-time behavioral data analysis.",
            "Facilitate sign-ups via a freemium model.",
            "Address data privacy concerns."
        ],
        audience_profile=(
            "Mid-sized tech companies (50-200 employees) seeking to increase team efficiency, reduce "
            "bottlenecks, improve data-driven decision-making, find affordable and scalable solutions, "
            "seamlessly integrate tools, and ensure data privacy."
        ),
        mandatory_inclusions={
            "value_prop": [
                "CloudFlow: Unlock peak team performance with AI-powered workflow automation. "
                "Get 10x more accurate insights and fix friction points others miss."
            ],
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
        recommended_formats=[
            "Webinars", "Case Studies", "Blog Posts", "Infographics",
            "Product Demos", "Whitepapers", "LinkedIn Articles", "Short Videos"
        ],
        channel_guidance={
            "LinkedIn": [
                "Target HR, operations, and tech decision-makers in mid-sized tech.",
                "Share thought leadership on AI-driven workflow automation.",
                "Run sponsored content showcasing customer success and product demos."
            ],
            "SaaS Blogs and Publications": [
                "Publish guest posts on workflow optimization and AI benefits.",
                "Participate in industry discussions.",
                "Secure product reviews and comparisons."
            ],
            "Webinars and Online Events": [
                "Showcase AI-driven workflow automation.",
                "Offer interactive product demos and Q&A.",
                "Partner with industry experts."
            ],
            "Partnerships with SaaS Providers": [
                "Co-market with complementary SaaS tools.",
                "Offer bundled solutions and integrated workflows.",
                "Cross-promote to relevant customer segments."
            ]
        },
        tone_and_voice="Professional, engaging, persuasive, data-driven, and slightly technical, while remaining accessible to non-technical decision-makers.",
        constraints=[
            "Avoid overly technical jargon that might alienate decision-makers.",
            "Do not make unsubstantiated claims about AI capabilities; always back up claims with data and proof points.",
            "Ensure all content aligns with data privacy and security best practices.",
            "Avoid direct comparisons with competitors that could be construed as disparaging."
        ]
    )

    # ----- 2. Final Content Output -----
    content = ContentCreationOutput(
        final_content="""Subject: Unlock Peak Performance: AI-Powered Workflow Automation for Your Tech Team

Hi [Name],

Are hidden workflow bottlenecks costing your tech team valuable time and resources? Traditional surveys often miss the mark, providing inaccurate or incomplete insights. Imagine knowing exactly where friction exists and having the power to eliminate it.

CloudFlow is an AI-powered workflow automation platform designed specifically for mid-sized tech companies like yours. Our unique approach analyzes real-time behavioral data, giving you **10x more accurate insights** than traditional methods.

With CloudFlow, you can:

* **Eliminate workflow bottlenecks:** AI-driven insights pinpoint inefficiencies, allowing you to optimize processes for maximum productivity.
* **Seamlessly integrate:** Connect CloudFlow with your existing tools and customize workflows to fit your unique needs, avoiding disruptive overhauls.
* **Gain clear, predictable value:** Our transparent and scalable pricing ensures you see a strong return on investment as you grow.

Worried about data privacy? Our AI-driven workflow analysis is secure and compliant, ensuring your team's data is protected.

Ready to see how CloudFlow can transform your team's performance? Sign up for a free demo today and discover the power of AI-driven workflow automation:

[Link to Demo]

Best regards,
The CloudFlow Team""",
        applied_angles=[
            "Quantify the hidden financial costs of inefficient workflows and highlight CloudFlow's ROI.",
            "Showcase the limitations of traditional surveys and the superior accuracy of CloudFlow's real-time behavioral analysis.",
            "Tailor messaging to the unique challenges of mid-sized tech, emphasizing scalability and customization."
        ],
        key_inclusions={
            "value_prop": [
                "CloudFlow: Unlock peak team performance with AI-powered workflow automation. "
                "Get 10x more accurate insights and fix friction points others miss."
            ],
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
        tone_and_voice="Professional, engaging, persuasive, data-driven, and slightly technical, while remaining accessible to non-technical decision-makers.",
        format="email"
    )

    return FullContentCreationResponse(
        brief=brief,
        content=content
    )

# ----------- LOCAL DEV MODE -----------
#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


















