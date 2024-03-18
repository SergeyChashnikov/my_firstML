# Импортируем библиотеки
import streamlit as st
from transformers import pipeline

st.title(" Переводчик с английского на русский ")
res = st.text_input("Пожалуйста введите текст")
if st.button("Перевести"):
    en_ru_translator = pipeline("translation",
                                 model="Helsinki-NLP/opus-mt-en-ru")
    trans = en_ru_translator(res)
    st.write("Перевод")
    st.text(trans[0]["translation_text"])
