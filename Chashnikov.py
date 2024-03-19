# Импортируем библиотеки
import streamlit as st
from transformers import pipeline

st.title(" Переводчик с английского на русский ")

text_input = st.text_input("Пожалуйста введите текст")
if st.button("Перевести"):
    en_ru_translator = pipeline("translation",
                                model="Helsinki-NLP/opus-mt-en-ru")
    translation_text = en_ru_translator(text_input)
    st.write("Перевод")
    st.text(translation_text[0]["translation_text"])
