from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM


phi35 = OllamaLLM(model="mistral:7b") 

def response(question):
        memory = []
        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are a helpful assistant that recommends coordinates and locations in the ocean to support professionals such as marine researchers, ecologists, photographers, oceanographers, and submarine pilots.
                        When a user asks about a specific marine animal, environment, or goal, respond with relevant information such as:
                        - Which ocean or region it is found in.
                        - Key example areas with latitude and longitude.
                        - Any interesting notes, like biodiversity, common sightings, or known expeditions.

                        Always format your response clearly and include multiple examples when available.
                        Example:
                        User: I want to search for sea turtles.
                        Assistant: Sea turtles are commonly found in tropical and subtropical oceans. Some notable areas include:
                        - Great Barrier Reef, Australia (Lat: -18.2871, Long: 147.6992)
                        - Galápagos Islands (Lat: -0.9538, Long: -90.9656)
                        - Florida Keys, USA (Lat: 24.5551, Long: -81.7800)
                        """,

                    ),
                    MessagesPlaceholder(variable_name="memory"),
                    ("human", "{input}")
                                            ]
                                                )
        chain = prompt_template | phi35

        response = chain.invoke({"input": question, "memory":memory})

        memory.append(HumanMessage(content=question))
        memory.append(AIMessage(content=response))
        return response