from groq import Groq

from app.utils.config import settings


class LLMService:
    """
    Service responsible for interacting with the Groq LLM.
    """

    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.MODEL_NAME

    def generate_answer(self, context: str, question: str) -> str:
        """
        Generate an answer using the retrieved document context.
        """

        prompt = f"""
You are an AI Technical Documentation Assistant.

Use ONLY the information provided in the context below.

Rules:
1. Answer ONLY from the provided context.
2. Do not use your own knowledge.
3. If the answer is not available in the context, reply exactly:
   "I couldn't find the answer in the uploaded document."
4. Be concise and technically accurate.
5. If the context is incomplete, mention that the available context is insufficient.
6. Do not mention that you are an AI unless explicitly asked.

-------------------------
Context:
{context}
-------------------------

Question:
{question}

Answer:
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You answer questions strictly from the provided document context."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=1024
        )

        return response.choices[0].message.content.strip()