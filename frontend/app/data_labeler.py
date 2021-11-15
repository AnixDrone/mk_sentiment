import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

URL = 'http://130.61.244.34:5000/'


def get_sentence():
    r = requests.get(f'{URL}random_sentence').json()
    if r is None:
        return None
    sentence = r['sentence']
    s_id = r['id']
    return sentence, s_id


if __name__ == '__main__':
    st.title('Label data for macedonian sentiment predictor')
    sentence_info = get_sentence()
    s = None
    if sentence_info is None:
        s = st.subheader('There is no unlabled sentences')
        st.button('Refresh')
    else:
        s = st.subheader(sentence_info[0])
        st.caption('Please choose sentiment for the presented sentence')

        col1, col2, col3 = st.columns(3)
        with col1:
            st.button('Positive sentiment', on_click=lambda: requests.get(
                f'{URL}sentence/{sentence_info[1]}/0'))

        with col2:
            st.button('Neutral sentiment', on_click=lambda: requests.get(
                f'{URL}sentence/{sentence_info[1]}/1'))

        with col3:
            st.button('Negative sentiment', on_click=lambda: requests.get(
                f'{URL}sentence/{sentence_info[1]}/2'))
