import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
def ask_amazon(query, context):

    system_prompt = """
You are Amazon AI, a helpful and professional product
assistant.
Your job is to answer customer questions using the
provided product context.
Instructions:
1. Use the provided context to answer the user's question.
2. Do not invent product details, prices, ratings, or features.
3. If the context does not contain enough information,
   clearly say that you do not have enough information.
4. Keep your answers clear, concise, and customer-friendly.
5. Do not claim that you can access live inventory,
   orders, or delivery information.
"""
    user_prompt = f"""
Customer Question:
{query}
Retrieved Product Context:
{context}
Answer the customer's question using the context above.
"""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content
print("Done All works perfectly")
