from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV
from sklearn.grid_search import RandomizedSearchCV
from sklearn.preprocessing import binarize
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

iris = load_iris()
# print iris.data
# print iris.feature_names
# print iris.target
# print type(iris.data)
# print type(iris.target)
# print iris.target_names
# print iris.data.shape

y = iris.target
X = iris.data
print X.shape
print y.shape
logreg = LogisticRegression()
knn = KNeighborsClassifier(n_neighbors=5)
lin = LinearRegression()
print knn
print logreg
knn.fit(X,y)
logreg.fit(X,y)
# print knn.predict([3,5,4,2])
X_new = [[3,5,4,2],[5,4,3,2]]
print knn.predict(X_new)
print logreg.predict(X_new)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=4)
# ypred = logreg.predict(X)
# print metrics.accuracy_score(y,ypred)
# ypred = knn.predict(X)
# print metrics.accuracy_score(y,ypred)
print X_train.shape
print X_test.shape
print y_train.shape
print y_test.shape
logreg.fit(X_train,y_train)
print logreg.intercept_
print logreg.coef_
print logreg.predict(X_test)[0:10]
print logreg.predict_proba(X_test)[0:10,:]
print logreg.predict_proba(X_test)[0:10,1]
y_pred_prob = logreg.predict_proba(X_test)[:,1]
# plt.rcParams['font.size'] = 14
# plt.hist(y_pred_prob,bins=8)
# plt.xlim(0,1)
# plt.show()


lin.fit(X_train,y_train)
print lin.intercept_
print lin.coef_
ypred = logreg.predict(X_test)
print metrics.accuracy_score(y_test,ypred)
knn.fit(X_train,y_train)
ypred = knn.predict(X_test)
print metrics.accuracy_score(y_test,ypred)
print metrics.mean_absolute_error(y_test,ypred)
print "MSE",(np.sqrt(metrics.mean_squared_error(y_test,ypred)))
k_range =range(1,31)
weight_option = ['uniform','distance']
param_grid = dict(n_neighbors=k_range,weights = weight_option)
grid = GridSearchCV(knn,param_grid,cv=10,scoring='accuracy')
grid.fit(X,y)
print grid.grid_scores_
print grid.grid_scores_[0].parameters
print grid.grid_scores_[0].cv_validation_scores
print grid.grid_scores_[0].mean_validation_score
grid_mean_scores = [result.mean_validation_score for result in grid.grid_scores_]
print grid_mean_scores
# plt.plot(k_range,grid_mean_scores)
# plt.show()

print grid.best_score_
print grid.best_params_
print grid.best_estimator_
print metrics.confusion_matrix(y_test,ypred)

# k_range =range(1,30)
# scores =[]
# for k in k_range:
# 	knn = KNeighborsClassifier(n_neighbors=k)
# 	knn.fit(X_train,y_train)
# 	ypred = knn.predict(X_test)
# 	scores.append(metrics.accuracy_score(y_test,ypred))

# plt.title("K selection")
# plt.plot(k_range,scores,k_range,[0.8]*len(k_range))
# plt.xlabel("value of K")
# plt.ylabel("test performance")
# plt.show()

data = pd.read_csv("C://Users/ma.xiaobo/Downloads/Advertising.csv")
print data.head()
print data.tail()
print data.shape
# sns.pairplot(data,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',size=7,aspect=0.7,kind='reg')
# sns.plt.show()
feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
X = data[['TV','Radio','Newspaper']]

print X.head()
print type(X)
print X.shape

y = data['Sales']
y = data.Sales

print y.head()
print type(y)
print y.shape
feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)
lin.fit(X_train,y_train)
ypred = lin.predict(X_test)
print np.sqrt((metrics.mean_squared_error(y_test,ypred)))
scores = cross_val_score(lin, X, y, scoring='mean_squared_error', cv=10)
print scores
mse_scores = -scores
print mse_scores
rmse_scores = np.sqrt(mse_scores)
print rmse_scores
print rmse_scores.mean()


kf = KFold(25, n_folds=5, shuffle=False)
print '{} {:^61} {}'.format('Iteration','Training set observations','Testing set observations')
for iteration,data in enumerate(kf,start=1):
	print '{:^9} {} {:^25}'.format(iteration,data[0],data[1])

iris = load_iris()
y = iris.target
X = iris.data
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
print scores
print scores.mean()

k_range = range(1,31)
k_scores =[]
for k in k_range:
	knn = KNeighborsClassifier(n_neighbors=k)
	scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
	k_scores.append(scores.mean())
print k_scores
# plt.plot(k_range,k_scores)
# plt.xlabel("value of K")
# plt.ylabel("CV Accuracy")
# plt.show()
