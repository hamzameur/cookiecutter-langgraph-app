import os
from typing import List

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from {{cookiecutter.package_name}}.constants import ENV_VAR_OPENAI_API_KEY
from typing_extensions import TypedDict

NODE_ANSWER_USER_QUERY: str = "answer_user_query"


class MyState(TypedDict):
    user_query: str
    chat_history: List[BaseMessage]
    response: str


def get_gpt_model() -> ChatOpenAI:
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ[ENV_VAR_OPENAI_API_KEY],
    )


def answer_user_query(state: MyState):
    user_query = state["user_query"]
    messages = state.get("chat_history", [])
    if not messages:
        messages = [SystemMessage("You are a helpful assistant.")]
    messages.append(HumanMessage(user_query))
    llm = get_gpt_model()
    ai_message = llm.invoke(messages)
    response = ai_message.content
    messages.append(ai_message)
    return {"response": response, "chat_history": messages}


def build_graph() -> CompiledStateGraph:
    workflow = StateGraph(MyState)
    workflow.add_node(NODE_ANSWER_USER_QUERY, answer_user_query)
    workflow.add_edge(START, NODE_ANSWER_USER_QUERY)
    workflow.add_edge(NODE_ANSWER_USER_QUERY, END)
    return workflow.compile()


graph = build_graph()
