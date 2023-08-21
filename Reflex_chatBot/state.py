import reflex as rx
import os
import openai

# import asyncio

openai.api_key = os.environ["OPENAI_API_KEY"]


class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    def answer(self):
        session = openai.ChatCompletion.create(
            model="gpt-35_turbo",
            message=[
                {
                    "role": "user",
                    "content": self.question,
                },
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )
        answer = ""
        self.chat_history.append((self.question, answer))
        for item in session:
            if hasattr(item.chices[0].delta, "content"):
                answer += item.choice[0].delta.content
                self.chat_history[-1] = (
                    self.question,
                    answer,
                )
                yield


# async def answer(self):
#     answer = "desconosco, no lo se."
#     self.chat_history.append(self.question, "")
#     for i in range(len(answer)):
#         await asyncio.sleep(0.1)
#         self.chat_hoistory[-1] = self.question, answer[:i]
#         yield
