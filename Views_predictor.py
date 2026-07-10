from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("youtube_views_200.csv")
#plt.scatter(df['Video_Length'],df['Views'])
#plt.show()

X=df[['VideoLength','UploadTime','TagsCount']]
y=df[['Views']]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=10)
prd=LinearRegression()
prd.fit(X_train,y_train)
print(prd.predict(X_test))
print(y_test)
print(prd.score(X_test,y_test))

