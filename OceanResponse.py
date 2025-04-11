import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

def response(question):
        memory = []
        llm = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768") 
        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a ocean specialist.",
                ),
                    MessagesPlaceholder(variable_name="memory"),
                    ("human", "{input}"),
            ]
        )
        chain = prompt_template | llm

        response = chain.invoke({"input": question, "memory":memory})

        memory.append(HumanMessage(content=question))
        memory.append(AIMessage(content=response))
        return response