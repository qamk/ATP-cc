import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import codecademylib3_seaborn
import glob

#for missing values in race
def race_nan(col):
  percent = 100
  races = ['Hispanic','Black','Pacific','Asian','White','Native']

  for race in races:
    if race == col:
      continue
    else:
      percent = percent - us_census[race]
  return percent

#combine files into a list
files = glob.glob('states[0-9].csv')

#turn files into pandas dataframes and concatenate them
dataset = [pd.read_csv(file) for file in files]

us_census = pd.concat(dataset)

#Convert the 'Income' col to float
us_census['Income'] = pd.to_numeric(us_census['Income'].replace('\$','',regex=True))

gender_pop_split = us_census['GenderPop'].str.split('_')
us_census['Men'] = pd.to_numeric(gender_pop_split.str.get(0).replace('\D','',regex=True))
us_census['Women'] = pd.to_numeric(gender_pop_split.str.get(1).replace('\D','',regex=True))

to_num_race= lambda row: pd.to_numeric(row.replace('%','',regex=True))

us_census['Hispanic'] = to_num_race(us_census['Hispanic'])
us_census['White'] = to_num_race(us_census['White'])
us_census['Black'] = to_num_race(us_census['Black'])
us_census['Native'] = to_num_race(us_census['Native'])
us_census['Asian'] = to_num_race(us_census['Asian'])
us_census['Pacific'] = to_num_race(us_census['Pacific'])

#Fill in missing values 
us_census = us_census.fillna(value={'Women':(us_census['TotalPop']-us_census['Men']), 'Hispanic':race_nan('Hispanic'),'Black':race_nan('Black'),'White':race_nan('White'),'Native':race_nan('Native'),'Pacific':race_nan('Pacific'),'Asian':race_nan('Asian')})


print(len(us_census))
us_census = us_census.drop_duplicates()
print(len(us_census))


#----------plots----------#
plt.scatter(us_census['Women'],us_census['Income'])
plt.title('Relationship between the number of women in a state and income')
plt.xlabel('Income')
plt.ylabel('# of Women')
plt.show()

fig, ((a1,a2,a3), (a4,a5,a6)) = plt.subplots(2,3,figsize=[10,7])
fig.suptitle('Graphs showing the proportion of each race and their frequency')
plt.subplots_adjust(hspace=0.5,wspace=0.5)
a1.hist(us_census['White'])
a1.set_title('White')
a1.set_ylabel('# of States')
a1.set_xlabel('Percentage (%)')

a2.hist(us_census['Black'])
a2.set_title('Black')
a2.set_ylabel('# of States')
a2.set_xlabel('Percentage (%)')

a3.hist(us_census['Native'])
a3.set_title('Native')
a3.set_ylabel('# of States')
a3.set_xlabel('Percentage (%)')

a4.hist(us_census['Asian'])
a4.set_title('Asian')
a4.set_ylabel('# of States')
a4.set_xlabel('Percentage (%)')

a5.hist(us_census['Hispanic'])
a5.set_title('Hispanic')
a5.set_ylabel('# of States')
a5.set_xlabel('Percentage (%)')

a6.hist(us_census['Pacific'])
a6.set_title('Pacific')
a6.set_ylabel('# of States')
a6.set_xlabel('Percentage (%)')


plt.show()



#----------print----------# 
print(us_census.head(10))
print(us_census.columns)
print(us_census.dtypes)
