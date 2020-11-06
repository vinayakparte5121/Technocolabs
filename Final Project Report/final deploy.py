# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:48:33 2020

@author: Vinu
"""

import streamlit as st
from PIL import Image
import pickle
def main():
    activities=['About','Toxic Comment Classification System','Developer']
    option=st.sidebar.selectbox('Menu Bar:',activities)
    if option=='About':
        html_temp = """
        <div style = "background-color: orange; padding: 10px;">
            <center><h1>ABOUT PROJECT</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        image=Image.open(r"C:\Users\Vinu\Desktop\Python\cls.jpeg")
        st.image(image,use_column_width=True)
        st.title("Problem Statement and Background:")
        st.subheader("Discussing things you care about can be difficult. The threat of abuse and harassment online means that many people stop expressing themselves and give up on seeking different opinions. Platforms struggle to effectively facilitate conversations, leading many communities to limit or completely shut down user comments.")
        st.header("The exact problem statement was thus as below:")
        st.subheader("Given a group of sentences or paragraphs, used as a comment by a user in an online platform, classify it to belong to one or more of the following categories — toxic, severe-toxic, obscene, threat, insult or identity-hate with either approximate probabilities or discrete values (0/1).")
        st.header("Data and Model used:")
        st.subheader("The Dataset used for this task is sourced from a Kaggle competition and is titled as the Jigsaw/Conversation AI Toxic Comment Classification Challenge Dataset. The creator have so far built a range of publicly available models served through the Perspective API and created this competition to enable participants to build a multi-headed model that is capable of detecting different types of toxicity like threats, obscenity, insults, and identity based hate better than their models. The dataset is composed of comments from Wikipedia’s talk page edits. The various categorizations for the comments are: toxic, severe toxic, obscene, threat, insult, and identity hate.The training dataset consists of 160k training samples and the test set consists of 153k samples.Understanding the dataset is an extremely vital task and there are several insights to be drawn from the dataset.")
        st.subheader("There were various models which could have been used but in my approach i used logistic Regression along with Tf-Idf. Tf-Idf stands for term frequency-inverse document frequency, and instead of calculating the counts of each word in each document of the dataset , it calculates the normalized count where each word count is divided by the number of documents this word appears. I’ve applied logistic regression which is a classification algorithm used to solve binary classification problems. The logistic regression classifier uses the weighted combination of the input features and passes them through a sigmoid function. Sigmoid function transforms any real number input, to a number between 0 and 1.")
    elif option=='Toxic Comment Classification System':
        st.title("Toxic Comment Classification System")
        f=open("toxic.pkl", "rb")
        model = pickle.load(f)
        v=pickle.load(f)
        st.header('Input Comment')
        text = st.text_input("Input text")
        lis=[]
        for i in range(6):
            lis.append(model[i].predict_proba(v.transform([text]))[:, 1])
        list=['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
        st.header('Output')
        for i in range(6):
            st.subheader(list[i])
            st.write(str(lis[i]))
        st.write('---')

    elif option=='Developer':
        st.info("Thank you for viewing")
        st.title('Prepared by:-')
        st.header('Vinayak Parte')
        st.subheader('Machine Learning Intern, Team 8, Technocolabs')
if __name__ == '__main__':
    main()