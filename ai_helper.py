import g4f
from g4f.client import Client
from translate import Translator

def get_ai_response(user_input):
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                'role': 'system',
                'content': "Ты - помощник для начинающих программистов. В ответе НЕ ИСПОЛЬЗУЙ маркировку текста Markdown. Перед началом выполнения кода здоровайся и описывай то, что ты будешь делать. Оставляй комментарии к ключевым моментам в коде. Перед блоком кода и после блока кода пиши ```"
            },
            {"role": "user", "content": user_input}
        ],
        stream=False,
        do_sample=True,
        temperature=0.2,
        top_p=0.9,
        top_k=50
    )
    return response


def extract_code_and_text(text):
    # Разделяем текст на части по тройным кавычкам
    parts = text.split('```')

    result = {}

    for i in range(len(parts)):
        if i % 2 == 0:
            key = f'before{i // 2 + 1}'
            value = parts[i].strip()
            result[key] = value
        elif i % 2 != 0:
            key = f'code{i // 2 + 1}'
            value = parts[i].strip()
            result[key] = value

    return result

def get_ai_image(user_input):

    client = Client()
    translator = Translator(from_lang="ru", to_lang="en")
    translation = translator.translate(user_input)
    response = client.images.generate(
        model="flux",
        prompt=translation,
        response_format="url"
    )
    image_url = response.data[0].url
    return(image_url)
