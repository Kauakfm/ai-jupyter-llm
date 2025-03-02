from openai import OpenAI
import os

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=200,
    temperature=0.1,
    messages=[
        { "role": "system", "content": "Você é um experiente programador. Retorne apenas código limpo e de qualidade." },
        { "role": "user", "content": "Escreva um codigo de Hello World em Python." }
    ]
)

print(completion.choices[0].message.content)