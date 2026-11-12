from google import genai
from app.config.config import settings


client = genai.Client(api_key=settings.gemini_api_key)


async def generate_content(prompt:str,response_schema=None):

    response = await client.aio.models.generate_content(
        model=settings.gemini_model_name,
        contents=prompt,
        config={
            'response_mime_type':"application/json",
            "response_json_schema":response_schema
        }
    )