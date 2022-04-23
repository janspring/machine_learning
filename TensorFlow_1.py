#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:11:55 2022

@author: jinzhang
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn
import urllib
import csv


dataset = "https://github.com/ageron/handson-ml/blob/master/datasets/lifesat/oecd_bli_2015.csv"
res = urllib.urlopen(dataset)
data = csv.reader(res)