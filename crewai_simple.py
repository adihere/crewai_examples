# 🤖 Leveraging CrewAI for a Multi-Agent Content Creation Pipeline

import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv
import logging

# 🔧 Setup & Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-5.4-nano'

# 👥 Agent Definitions

# 📝 Planner Agent
planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="Expert content strategist crafting outlines for {topic}",
    allow_delegation=False,
    verbose=True
)

# ✍️ Writer Agent
writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate opinion piece about {topic}",
    backstory="Skilled writer creating compelling content based on planner's outline",
    allow_delegation=False,
    verbose=True
)

# 🖋️ Editor Agent
editor = Agent(
    role="Editor",
    goal="Polish and refine the blog post for publication",
    backstory="Experienced editor ensuring quality and alignment with brand voice",
    allow_delegation=False,
    verbose=True
)

# 📋 Task Definitions

# 🗺️ Planning Task
plan = Task(
    description="Create a comprehensive content plan for {topic}",
    expected_output="Detailed outline with audience analysis and SEO keywords",
    agent=planner
)

# 📝 Writing Task
write = Task(
    description="Craft a compelling blog post on {topic} using the content plan",
    expected_output="Well-structured markdown blog post ready for editing",
    agent=writer
)

# ✏️ Editing Task
edit = Task(
    description="Proofread and refine the blog post for publication",
    expected_output="Polished blog post in markdown format, publication-ready",
    agent=editor
)

# 🚀 Crew Assembly and Execution
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

# 🏃‍♂️ Run Function with Logging
def run_crew_with_logging(topic):
    logger.info(f"🎬 Starting CrewAI process for topic: {topic}")
    try:
        result = crew.kickoff(inputs={"topic": topic})
        logger.info("✅ CrewAI process completed successfully")
        return result
    except Exception as e:
        logger.error(f"❌ Error occurred during CrewAI process: {str(e)}")
        raise

# 🚀 Main Execution
topic = "Chatbots are so 2024 - 2025 is about leveraging GenAI agents"
try:
    result = run_crew_with_logging(topic)
    logger.info("🏁 Result obtained successfully")
    print(result)
except Exception as e:
    logger.error(f"💥 Failed to obtain result: {str(e)}")
