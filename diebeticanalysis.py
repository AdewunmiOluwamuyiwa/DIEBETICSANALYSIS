import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np


#read a csv file
#import csv file
#convert file to dataframe

df = pd.read_csv("diabetes.csv")
st.write(df.head(5))

