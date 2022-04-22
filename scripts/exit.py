import streamlit as st
import os
import pandas as pd


def read_tweets():
    tweets_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'tweets.csv')
    df = pd.read_csv(tweets_file)
    return df


def app():
    wrapper()


def wrapper():
    #st.write(st.session_state)
    df = read_tweets()
    for tweets, label in zip(st.session_state['tweets'][:-1], st.session_state['labels']):
        df.loc[df.clean_text == tweets, 'label'] = label
    tweets_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'tweets.csv')
    df.to_csv(tweets_file, index=False)

    st.title('Thank you for helping us to label the data!')
    #st.write(st.session_state)
