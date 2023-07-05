import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

model = os.environ["MODEL"]


def ask_question(question):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    )

    response = completion.choices[0].message.content

    return response


if __name__ == "__main__":
    question = input()

    res = ask_question(question)

    print(res)
