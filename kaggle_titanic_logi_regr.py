#import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv("passengers.csv")


# Update sex column to numerical
"""passengers['Sex'] = passengers['Sex'].replace('female',1,regex=True)
passengers['Sex'] = passengers['Sex'].replace('male',0,regex=True)"""
passengers['Sex'] = passengers['Sex'].map({'male':0,'female':1})
# Fill the nan values in the age column
passengers= passengers.fillna(value={'Age':passengers['Age'].mean()})
# Create a first class column
class_1 = lambda row: 1 if row == 1 else 0

passengers['FirstClass'] = passengers['Pclass'].apply(class_1)


# Create a second class column
class_2 = lambda row: 1 if row == 2 else 0
passengers['SecondClass'] = passengers['Pclass'].apply(class_2)
print(passengers.head(10), passengers.dtypes)

# Select the desired features
features = np.array(passengers[['Sex','Age','FirstClass','SecondClass']])
survival = np.array(passengers['Survived'])

# Perform train, test, split
features_train,features_test,survival_train,survival_test = train_test_split(features,survival,test_size=.2,random_state=45)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)


# Create and train the model
model = LogisticRegression()
model.fit(features_train,survival_train)



# Score the model on the train data
print(model.score(features_train,survival_train))

# Score the model on the test data
print(model.score(features_test,survival_test))

# Analyze the coefficients
print(model.coef_)

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([0.0,22.0,1.0,0.0])

# Combine passenger arrays
sample_passengers = np.array([Jack,Rose,You])
print(sample_passengers)


# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
sample_predict = model.predict_proba(sample_passengers)
print("Prediction results: ",sample_predict)
