# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 17:21:23 2025

@author: zegar
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sn


df=pd.read_csv("estudiantes_notas_finales_arboles.csv")