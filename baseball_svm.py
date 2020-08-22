import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary #made by cc to visualise the SVM
from players import aaron_judge, jose_altuve, david_ortiz
import numpy as np


def svc_classify(df,fig):
  fig, ax = plt.subplots()
#print(aaron_judge['description'].unique())
  map_type = lambda row: row.map({'S':1,'B':0})
  df['type'] = map_type(df['type'])
#print(aaron_judge['type'])
#print(aaron_judge['plate_x'])
  df = df.dropna(subset=['plate_x','plate_z','type'])

  ax.scatter(df['plate_x'],df['plate_z'],c=df['type'],cmap=plt.cm.coolwarm,alpha=.25)

  training_set,validation_set = train_test_split(df,random_state=1)

  classifier = SVC(kernel = 'rbf',gamma=50,C=2)
  classifier.fit(training_set[['plate_x','plate_z']],training_set['type'])
  #draw_boundary(ax,classifier)
  plt.show()
  return classifier.score(validation_set[['plate_x','plate_z']],validation_set['type'])

print(svc_classify(aaron_judge,plt.figure()))
print(svc_classify(david_ortiz,plt.figure()))
