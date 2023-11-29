# Импортируем библиотеки
import io
import streamlit as st
import transformers
from transformers import pipeline

st.title(' Переводчик с английского на русский ')

res = st.text_input('Пожалуйста введите текст')
if st.button('Перевести'):
    en_ru_translator = pipeline("translation_en_to_ru", 'Helsinki-NLP/opus-mt-en-ru')
    trans = en_ru_translator(res)
    st.write('Перевод')
    for i in trans:
        st.write(i['translation_text'])
