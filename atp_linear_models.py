#import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# load and investigate the data here:

df = pd.read_csv("tennis_stats.csv")

print(df.head(5),df.dtypes)

# perform exploratory analysis here:
fig, axs = plt.subplots(3,2, figsize=(10,7))
plt.subplots_adjust(hspace=0.4)
axs[0,0].scatter(df['FirstServePointsWon'],df['Wins'],c='#aa42cc',alpha=0.4)
axs[0,0].set_title("First Serve Points Won vs Wins")
axs[0,1].scatter(df['BreakPointsSaved'],df['Wins'],c='#dea32c',alpha=0.4)
axs[0,1].set_title("Break Points Saved vs Wins")
axs[1,0].scatter(df['Aces'],df['Wins'],c='#e81d13',alpha=0.4)
axs[1,0].set_title("Aces vs Wins")
axs[1,1].scatter(df['ServiceGamesWon'],df['Wins'],c='#3faceb',alpha=0.4)
axs[1,1].set_title("Service Games Won vs Wins")
axs[2,0].scatter(df['ReturnPointsWon'],df['Wins'],c='#ca2bff',alpha=0.4)
axs[2,0].set_title("Return Points Won vs Wins")
axs[2,1].scatter(df['DoubleFaults'],df['Wins'],c='#3e1ff0',alpha=0.4)
axs[2,1].set_title("Double Faults vs Wins")
plt.show()


## perform single feature linear regressions here:
x = np.array(df['DoubleFaults'])
y = np.array(df['Wins'])

x=x.reshape(-1,1)
y=y.reshape(-1,1)
print(y[0:4],"\n",x[0:4])

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size = 0.8, test_size = 0.2, random_state = 24)

lr = LinearRegression()

slr = lr.fit(x_train,y_train)
slr_yhat = slr.predict(x_test)

print("SLR with double faults IV (coef,incept,R2):", slr.coef_,slr.intercept_,slr.score(x_test,y_test))

fig2 = plt.figure()
fig2, axs2 = plt.subplots(1,2,figsize=(10,7))
plt.subplots_adjust(hspace=0.6)
axs2[0].scatter(slr_yhat,y_test,alpha=0.4,c=['#3244da'])
axs2[0].set_title("SLR showing Double Faults IV and # Wins")
axs2[0].set_xlabel("Predicted")
axs2[0].set_ylabel("Actual")

#next model
x2 = np.array(df['FirstServePointsWon'])
x2 = x2.reshape(-1,1)

x_train2,x_test2,y_train2,y_test2 = train_test_split(x2,y,train_size = 0.8, test_size = 0.2, random_state = 24)

slr2 = lr.fit(x_train2,y_train2)
slr_yhat2 = slr2.predict(x_test2)
axs2[1].scatter(slr_yhat2,y_test,alpha=0.4,c=['#e2445a'])
axs2[1].set_title("SLR Showing First Serve Points Won and # Wins")
axs2[1].set_xlabel("Predicted")
axs2[1].set_ylabel("Actual")
plt.show()

print("SLR with First Serve Points IV (coef,incept,R2):", slr2.coef_,slr2.intercept_,slr2.score(x_test2,y_test))
## perform two feature linear regressions here:
X_2_IV = np.array(df[['Year','Aces']])
#X_2_IV = X_2_IV.reshape(-1,1)

X_2_IV2 = np.array(df[['ReturnGamesWon','BreakPointsSaved']])
#X_2_IV2 = X_2_IV2.reshape(-1,1)

X_2_IV3 = np.array(df[['TotalPointsWon','Losses']])
#X_2_IV3 = X_2_IV3.reshape(-1,1)

y = np.array(df['Winnings'])
y= y.reshape(-1,1)


#Winnings = Year + Aces
X_train,X_test,y_train,y_test = train_test_split(X_2_IV,y,train_size = 0.8, test_size = 0.2, random_state = 24)

#Winnings = Return Games Won + Break Points Saved
X_train2,X_test2,y_train2,y_test2 = train_test_split(X_2_IV2,y,train_size = 0.8, test_size = 0.2, random_state = 24)

#Winnings = Points Won + Losses
X_train3,X_test3,y_train3,y_test3 = train_test_split(X_2_IV3,y,train_size = 0.8, test_size = 0.2, random_state = 24)

#Winnings = Year + Aces
mlr = lr.fit(X_train,y_train)
mlr_yhat = mlr.predict(X_test)

#Winnings = Return Games Won + Break Points Saved
mlr2 = lr.fit(X_train2,y_train2)
mlr_yhat2 = mlr.predict(X_test2)

#Winnings = Points Won + Losses
mlr3 = lr.fit(X_train3,y_train3)
mlr_yhat3 = mlr.predict(X_test3)

print("Coefficients and Score for MLR... \nWinnings = Year + Aces: ", mlr.coef_,mlr.score(X_test,y_test))
print("\nCoefficients and Score for MLR... \nWinnings = Return Games Won + Break Points Saved: ", mlr2.coef_,mlr2.score(X_test2,y_test2))
print("\nCoefficients and Score for MLR... \nWinnings = Points Won + Losses: ", mlr3.coef_,mlr3.score(X_test3,y_test3))


## perform multiple feature linear regressions here:

X_n_IV = np.array(df[["Year","Aces","TotalPointsWon","ServiceGamesPlayed"]])
X_n_IV2 = np.array(df[['Losses','Ranking','FirstServe','BreakPointsConverted']])

#Winnings = Year + Aces + Points + # Service Games
X_n_train, X_n_test, y_train, y_test = train_test_split(X_n_IV,y,train_size=0.8,test_size=0.2,random_state=44)

#Winnings = Losses + Ranking + First Serve % + Break Points Convrtd
X_n_train2, X_n_test2, y_train2, y_test2 = train_test_split(X_n_IV2,y,train_size=0.8,test_size=0.2,random_state=44)

#Winnings = Year + Aces + Points + # Service Games
mlr4 = lr.fit(X_n_train,y_train)
mlr_yhat4 = mlr.predict(X_n_test)

#Winnings = Losses + Ranking + First Serve % + Break Points Convrtd
mlr5 = lr.fit(X_n_train2, y_train2)
mlr_yhat4 = mlr.predict(X_n_test2)

print("Coefficients and Score for MLR... \nWinnings = Year + Aces+ Points + # Service Games: ", mlr4.coef_,mlr4.score(X_n_test,y_test))
print("\nCoefficients and Score for MLR... \nWinnings = Losses + Ranking + First Serve (proportion) + Break Points Converted: ", mlr5.coef_,mlr5.score(X_n_test2,y_test2))


















