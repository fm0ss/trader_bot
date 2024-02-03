from newsplease import NewsPlease
import os
 
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="Google Search",
    description="Search Google for recent results.",
    func=search.run,
)

# Finding financial news

os.environ["OPENAI_API_KEY"] = "{OpenAPI KEY Here}"
os.environ["SERPAPI_API_KEY"] = "{SERPAPI KEY Here}"

llm = OpenAI(temperature=0)

tools = load_tools([tool], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("Is this likely to be a news article it may be a news page and link to articles but not be an article, however it may be a news article which also happens to link to other news articles Y/N? https://www.reuters.com/markets/")


