# backend/agents/nerva_agent.py
from langgraph.graph import Graph
from langgraph.nodes import ToolNode, LLMNode
from integrations.notion_client import create_notion_page
from integrations.figma_client import create_figma_wireframe

def build_nerva_agent():
    g = Graph()

    llm = LLMNode(model="gpt-4o-mini", system_prompt="You are NERVA, a creative AI workspace agent.")
    notion_tool = ToolNode(tool=create_notion_page, name="NotionCreator")
    figma_tool = ToolNode(tool=create_figma_wireframe, name="FigmaWireframe")

    g.add_node(llm)
    g.add_node(notion_tool)
    g.add_node(figma_tool)

    g.connect(llm, notion_tool)
    g.connect(notion_tool, figma_tool)

    return g
