"""Data Labeler."""
import streamlit as st
import requests


URL = 'http://130.61.244.34:5000/'


def get_sentence():
    """Get random sentence from the database.

    :return: Sentence and its id
    :rtype: tuple
    """
    req = requests.get(f'{URL}random_sentence', timeout=500).json()
    if req is None:
        return None
    sentence = req['sentence']
    s_id = req['id']
    return sentence, s_id


if __name__ == '__main__':
    st.title('Label data for macedonian sentiment predictor')
    sentence_info = get_sentence()
    SOME_THING = None
    if sentence_info is None:
        SOME_THING = st.subheader('There is no unlabled sentences')
        st.button('Refresh')
    else:
        SOME_THING = st.subheader(sentence_info[0])
        st.caption('Please choose sentiment for the presented sentence')

        col1, col2, col3 = st.columns(3)
        with col1:
            st.button('Positive sentiment', on_click=lambda: requests.get(
                f'{URL}sentence/{sentence_info[1]}/0', timeout=500))

        with col2:
            st.button('Neutral sentiment', on_click=lambda: requests.get(
                f'{URL}sentence/{sentence_info[1]}/1', timeout=500))

        with col3:
            st.button('Negative sentiment', on_click=lambda: requests.get(
                f'{URL}sentence/{sentence_info[1]}/2', timeout=500))
