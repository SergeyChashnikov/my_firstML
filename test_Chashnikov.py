from streamlit.testing.v1 import AppTest


def test_text_input():

    at = AppTest.from_file("Chashnikov.py")

    at.run(timeout=30)

    print(at.main)
    text = "Good evening my little friend"
    at.text_input[0].set_value(text)
    at.button[0].click().run(timeout=60)

    print(at.main)
    print(at.main.markdown[1].value)
    #print(at.markdown[0])
    #print(at.markdown[1].value)

    #assert at.markdown[1].value == "Добрый вечер, мой маленький друг."

#test_text_input()
