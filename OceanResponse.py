from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM


phi35 = OllamaLLM(model="phi3.5:3.8b") 

def response(question):
        memory = []
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
        chain = prompt_template | phi35

        response = chain.invoke({"input": question, "memory":memory})

        memory.append(HumanMessage(content=question))
        memory.append(AIMessage(content=response))
        return response