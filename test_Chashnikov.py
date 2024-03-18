from streamlit.testing.v1 import AppTest


def test_text_input():

    at = AppTest.from_file("Chashnikov.py")

    at.run(timeout=30)

    print(at.main)
    text = "Good evening my little friend"
    at.text_input[0].set_value(text)
    at.button[0].click().run(timeout=60)

    #print(at.main.children[1])
    print(at.main)
    print(at.main.children[3])
    print(at.main.children[3].value)
    print(at.text)
    #print(at.markdown[1].value)
    print(at.main)

    assert at.main.children[3].value == "Добрый вечер, мой маленький друг."

#test_text_input()
