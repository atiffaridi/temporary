# Author: Atif Faridi
# Objective: Parameter estimation for Support Vector Regression Using Grid Search

# importing required modules
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
import datetime
import time

# name of file in current working directory
path = 'INFY.NS.csv'

# open file at path
data_fl = open(path, 'r')

# read file contents in string format
data = data_fl.read()

# parse csv file content to make dataset
dataset = [row.split(',') for row in data.split('\n') if len(row) > 0]

# extracting date and closing price as training features
# converting date time into timestamp
dataset_x = [[int(datetime.datetime.strptime(
    dataset[i_row][0], '%Y-%m-%d').timestamp()/(24*3600)), float(dataset[i_row][4])]
             for i_row in range(1, len(dataset))]

# extracting training target feature
dataset_y = [float(dataset[i_row][1]) for i_row in range(1, len(dataset))]

# initializing parameters for grid search
parametrss = {"gamma": [0.1, 0.2, 0.3], 'kernel': ['rbf', 'sigmoid', 'linear']}

# initializing svr_model with grid search parameters
svr_model = GridSearchCV(SVR(C=1), cv=5, param_grid=parametrss)

# capture starting time before fitting svr model
t0 = time.time()

# fitting svr_model for training data
svr_model.fit(dataset_x, dataset_y)

# capturing svr fitting time
svr_fit_time = time.time() - t0

best_model = svr_model.best_estimator_
print('Parameters for best support vector regression model:--> ', best_model)

