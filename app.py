from flask import Flask, request, render_template, jsonify
import ai_helper
import webview
import pygments
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.util import ClassNotFound
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# Создаем экземпляр приложения Flask
#1
app = Flask(__name__)
app.config["DEBUG"] = True

window_option = {
    'fullscreen': False,
    'frameless': False
}

window = webview.create_window('LearnMate', app, maximized=True, resizable=True)

def highlight_code(code, language=None):
    try:
        lexer = get_lexer_by_name(language)
    except ClassNotFound:
        lexer = guess_lexer(code)

    formatter = HtmlFormatter()  # Без <div> вокруг кода
    highlighted = pygments.highlight(code, lexer, formatter)

    # Оборачиваем код и добавляем кнопку копирования
    html_with_copy = f"""
    <button class="copy-button"><i class="fa-solid fa-copy"></i></button>
    <pre class="highlight">
        <code>{highlighted}</code>
    </pre>
    """
    return html_with_copy

# Функция для генерации ответа от ИИ
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        response_white = ai_helper.get_ai_response(user_text)
        response = ai_helper.extract_code_and_text(response_white)

        response_ai = ''

        # Проверка и добавление текста и кода отдельно
        if 'before1' in response:
            ai_text1 = response['before1']
            response_ai += ai_text1
        if 'code1' in response:
            ai_code1 = highlight_code(response['code1'], 'python')
            response_ai += ai_code1

        if 'before2' in response:
            ai_text2 = response['before2']
            response_ai += ai_text2
        if 'code2' in response:
            ai_code2 = highlight_code(response['code2'], 'python')
            response_ai += ai_code2

        if 'before3' in response:
            ai_text3 = response['before3']
            response_ai += ai_text3
        if 'code3' in response:
            ai_code3 = highlight_code(response['code3'], 'python')
            response_ai += ai_code3

        if 'before4' in response:
            ai_text4 = response['before4']
            response_ai += ai_text4
        if 'code4' in response:
            ai_code4 = highlight_code(response['code4'], 'python')
            response_ai += ai_code4

        if 'before5' in response:
            ai_text5 = response['before5']
            response_ai += ai_text5
        if 'code5' in response:
            ai_code5 = highlight_code(response['code5'], 'python')
            response_ai += ai_code5

        if 'before6' in response:
            ai_text6 = response['before6']
            response_ai += ai_text6
        if 'code6' in response:
            ai_code6 = highlight_code(response['code6'], 'python')
            response_ai += ai_code6

        if 'before7' in response:
            ai_text7 = response['before7']
            response_ai += ai_text7
        if 'code7' in response:
            ai_code7 = highlight_code(response['code7'], 'python')
            response_ai += ai_code7

        # Возвращаем ответ в виде HTML
        return response_ai
    else:
        return render_template('index.html')

@app.route('/generate_image', methods=['GET', 'POST'])
def generate_image():
    if request.method == 'POST':
        description = request.form['description']
        generated_image = ai_helper.get_ai_image(description)
        return f'<img src={generated_image} />'
    else:
        return render_template('image_gen.html')

@app.route('/FAQ')
def faq():
    return render_template('FAQ.html')

# Страницa About.
@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    #app.run(debug=True)
    webview.start()