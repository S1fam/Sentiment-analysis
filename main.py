import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import glob

analyzer = SentimentIntensityAnalyzer()

folder_path = 'D:/Python/BBB/BookSentimentAnalysis/diary'  # your absolute path to text files for analysis
file_contents = {}

file_list = glob.glob(os.path.join(folder_path, '*.txt'))

names = []
for file_path in file_list:
    with open(file_path, "r") as file:
        file_name = os.path.basename(file_path)
        names.append(file_name.split(".")[0])  # we could also use strip
        file_contents[file_name] = file.read()

print(names)

positivity = []
negativity = []
for file_name, content in file_contents.items():
    scores = analyzer.polarity_scores(content)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])
    print(scores)


st.title("Diary Tone")


st.header("positivity")
figure1 = px.line(x=names, y=positivity, labels={"x": "writing", "y": "positivity"})
st.plotly_chart(figure1)


st.header("Negativity")
figure2 = px.line(x=names, y=negativity, labels={"x": "writing", "y": "positivity"})
st.plotly_chart(figure2)
