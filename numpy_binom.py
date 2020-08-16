#import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = np.array(['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos'])

total_ceballos = np.sum(survey_responses=='Ceballos')
print(total_ceballos)
percentage_ceballos = np.mean(survey_responses=='Ceballos')
print(percentage_ceballos)
print(len(survey_responses))
possible_surveys =\
np.random.binomial(70,0.54,size=10000)/70.

print(possible_surveys)
ceballos_loss_surveys=np.mean(possible_surveys<0.5)
print(ceballos_loss_surveys)

large_survey= np.random.binomial(7000,0.54,size=10000)/7000.
ceballos_loss_surveys_new = np.mean(large_survey<0.5)
print(ceballos_loss_surveys_new)

plt.hist(possible_surveys, range=(0,1),bins=20)

plt.show()

