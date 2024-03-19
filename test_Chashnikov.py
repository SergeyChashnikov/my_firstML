from streamlit.testing.v1 import AppTest


# Тест для проверки заголовка
def test_title():

    at = AppTest.from_file("Chashnikov.py")
    at.run(timeout=30)
    
    assert at.title[0].value == "Переводчик с английского на русский"


# Тест для проверки перевода
def test_text_input():

    at = AppTest.from_file("Chashnikov.py")
    at.run(timeout=30)
    text = "Good evening my little friend"
    at.text_input[0].set_value(text).run()
    at.button[0].click().run(timeout=60)

    assert at.text[0].value == "Добрый вечер, мой маленький друг."
