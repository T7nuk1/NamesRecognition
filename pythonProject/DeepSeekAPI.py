#sk-510e40b434144be49c300664dabba372
from openai import OpenAI
from urllib3 import request

client = OpenAI(api_key="sk-510e40b434144be49c300664dabba372", base_url="https://api.deepseek.com")


first_name_request = ("Определи, какие из этих слов могут быть именем:"
           "Дополнителные условия:"
           "- Имена не могут быть в уменьшительно-ласкательной форме"
           "- Не изменяй слова"
           "- В ответ пришли строго только список слов, не присылай свои комментарии."
           "Вот список слов: \n")

last_name_request = ("Определи, какие из этих слов могут быть фаимилией:"
           "Дополнителные условия:"
           "- Не изменяй слова"
           "- В ответ пришли строго только список слов, не присылай свои комментарии."
           "Вот список слов: \n")

def SendNameRecognitionRequest(input_names: str) -> str:
    print("[DeepSeekApi]: Отправка запроса в Deepseek..")
    request_message = first_name_request + input_names
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": request_message},
    ],
    stream=False
    )

    return response.choices[0].message.content

def SendLastNameRecognitionRequest(input_names: str) -> str:
    print("[DeepSeekApi]: Отправка запроса в Deepseek..")
    request_message = last_name_request + input_names
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": request_message},
        ],
        stream=False
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    with open("./last_names.txt", "r", encoding="utf-8") as black_file:
        black_text = black_file.read()
    with open("./results/last_names_ai_processed.txt", "w", encoding="utf-8") as Natasha_file:
    #   Natasha_text = SendLastNameRecognitionRequest(black_text)
       Natasha_file.writelines(black_text)