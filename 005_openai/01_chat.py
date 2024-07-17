#%%
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path="../.env")  # take environment variables

#%%
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "The coffee is extremely ...",
        }
    ],
    model="gpt-3.5-turbo",
)

#%%
print(completion.choices[0].message.content)
