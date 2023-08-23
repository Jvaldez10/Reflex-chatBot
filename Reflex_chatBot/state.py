import reflex as rx
import os
import openai

# import asyncio
# openai.API_KEY = os.environ["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"]
# openai.api_key = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]


class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot has some brains now!
        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.question}],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))
        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.question, answer)
                yield


# async def answer(self):
#     answer = "desconosco, no lo se."
#     self.chat_history.append(self.question, "")
#     for i in range(len(answer)):
#         await asyncio.sleep(0.1)
#         self.chat_hoistory[-1] = self.question, answer[:i]
#         yield
