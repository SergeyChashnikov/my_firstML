# Импортируем библиотеки
import streamlit as st
from transformers import pipeline


# Создаем заголовок
st.title(" Переводчик с английского на русский ")
# Создаем текстовое поле для ввода текста
text_input = st.text_input("Пожалуйста введите текст")
# При нажатии кнопки "Перевести" создается
# модель с помощью pipline, выполняется перевод
if st.button("Перевести"):
    en_ru_translator = pipeline("translation",
                                model="Helsinki-NLP/opus-mt-en-ru")
    translation_text = en_ru_translator(text_input)
    st.write("Перевод")
    st.text(translation_text[0]["translation_text"])
