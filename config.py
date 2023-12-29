import openai
import os
import dotenv
import elevenlabs

dotenv.load_dotenv()

elevenlabs.set_api_key(os.environ["ELEVENLABS"])
openai.api_key = os.environ["OPENAI_API_KEY"]
