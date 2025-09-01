import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-2.5-flash')

def response(question):
    try:
        prompt = f"""You are a helpful assistant that recommends coordinates and locations in the ocean to support professionals such as marine researchers, ecologists, photographers, oceanographers, and submarine pilots.

    When a user asks about a specific marine animal, environment, or goal, respond with relevant information such as:
    - Which ocean or region it is found in.
    - Key example areas with latitude and longitude.
    - Any interesting notes, like biodiversity, common sightings, or known expeditions.

    Always format your response clearly and include multiple examples when available.

    Now, respond to the following question:

    User: {question}
    Assistant:"""

        # Generate content using Gemini
        response = model.generate_content(prompt)
        
        # Return the generated text
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"
