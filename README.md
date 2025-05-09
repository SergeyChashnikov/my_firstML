My homework 4

Translation application

The application is designed to translate text from English to Russian. 
Created based on the "Helsinki-NLP/opus-mt-en-ru" model. 
To run, you need to install transformers, streamlit, tensorflow, sentencepiece.


graph TD;
    A["VideoReader<br>Считывает кадры из видеофайла"] --> B["DetectionTrackingNodes<br>Реализует детектирование людей + трекинг"];
    B --> C["TrackerInfoUpdateNode<br>Обновляет информацию об актуальных треках"];
    C --> D["CalcStatisticsNode<br>Вычисляет загруженность/нарушение зон"];
    D --sent_info_db==False --> F;
    D --sent_info_db==True --> E["SentInfoDBNode<br>Отправляет результаты в базу данных"];
    E --> F["ShowNode<br>Отображает результаты на экране"];
    F --save_video==True --> H["VideoSaverNode<br>Сохраняет обработанные кадры"];
    F --show_in_web==True & save_video==False --> L["FlaskServerVideoNode<br>Обновляет кадры в веб-интерфейсе"];
    H --show_in_web==True --> L
