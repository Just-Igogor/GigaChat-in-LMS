"""Пример работы с чатом через gigachain"""
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='NjU0YzUyYmQtOWVlNC00ZmQ5LWIyMmQtMjA5Y2Q5ZDQ1OWViOjhhYjg1NDYzLWViZDUtNGFhNC05Yzk4LTJjNzMyNmQwYWZmYw==', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]

while(True):
    # Ввод пользователя
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    # Ответ сервиса
    print("Bot: ", res.content)