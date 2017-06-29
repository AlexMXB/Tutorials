from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
# iris = load_iris()
# y = iris.target
# X = iris.data
# print pd.DataFrame(X,columns=iris.feature_names).head()
# print y
# knn = KNeighborsClassifier()
# knn.fit(X,y)
# print knn
# res = knn.predict([[3,5,4,2]])
# print res
# simple_train = ['call you tonight','call me a cab','please call me...please']
# is_desperate = [0,0,1]
# vect = CountVectorizer()
# vect.fit(simple_train)
# print vect.get_feature_names()
# simple_train_dtm = vect.transform(simple_train)
# print simple_train_dtm
# print type(simple_train_dtm)
# print simple_train_dtm.toarray()
# print pd.DataFrame(simple_train_dtm.toarray(),columns=vect.get_feature_names())
# knn=KNeighborsClassifier(n_neighbors=1)
# knn.fit(simple_train_dtm,is_desperate)
# simple_test = ["please don't call me"]
# simple_test_dtm = vect.transform(simple_test)
# print simple_test_dtm
# print simple_test_dtm.toarray()
# print pd.DataFrame(simple_test_dtm.toarray(),columns=vect.get_feature_names())
# print knn.predict(simple_test_dtm)

url = 'https://raw.githubusercontent.com/justmarkham/pydata-dc-2016-tutorial/master/sms.tsv'
sms = pd.read_table(url,header=None,names=['label','message'])
print sms.shape
print sms.head(10)
print sms.label.value_counts()
sms['label_num'] = sms.label.map({'ham':0,'spam':1})
print sms.head(10)
X = sms.message
y = sms.label_num
print X.shape
print y.shape
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)
print X_train.shape
print y_train.shape
print X_test.shape
print y_test.shape
vect = CountVectorizer()
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
print X_train_dtm
X_test_dtm = vect.transform(X_test)
print X_test_dtm
nb = MultinomialNB()
nb.fit(X_train_dtm,y_train)
y_pred_class = nb.predict(X_test_dtm)
print metrics.accuracy_score(y_test,y_pred_class)
print metrics.confusion_matrix(y_test,y_pred_class)
print 1-sms.label_num.mean()
print metrics.roc_auc_score(y_test,y_pred_class)
print nb.predict_proba(X_test_dtm)[:,1]
logreg = LogisticRegression()
logreg.fit(X_train_dtm,y_train)
y_pred_class = logreg.predict(X_test_dtm)
print metrics.accuracy_score(y_test,y_pred_class)
print metrics.confusion_matrix(y_test,y_pred_class)
print 1-sms.label_num.mean()
print metrics.roc_auc_score(y_test,y_pred_class)
print logreg.predict_proba(X_test_dtm)[:,1]
X_train_tokens = vect.get_feature_names()
print len(X_train_tokens)
print X_train_tokens[:50]
print X_train_tokens[-50:]
print nb.feature_count_
print nb.feature_count_.shape
ham_token_count = nb.feature_count_[0,:]
print ham_token_count
spam_token_count = nb.feature_count_[1,:]
print spam_token_count
tokens = pd.DataFrame({'token':X_train_tokens,'ham':ham_token_count,'spam':spam_token_count})
print tokens.head()
print tokens.sample(5,random_state=6)
print nb.class_count_
tokens['ham'] = tokens.ham + 1
tokens['spam'] = tokens.spam + 1
print tokens.sample(5,random_state=6)
tokens['ham'] = tokens.ham / nb.class_count_[0]
tokens['spam'] = tokens.spam / nb.class_count_[1]
print tokens.sample(5,random_state=6)
tokens['spam_ratio'] = tokens.spam / tokens.ham
print tokens.sample(5,random_state=6)
print tokens.sort_values('spam_ratio',ascending=False)
print tokens[tokens.token=='claim'].spam_ratio
vect = CountVectorizer(stop_words='english')
vect = CountVectorizer(ngram_range=(1, 2))
vect = CountVectorizer(max_df=0.5)
vect = CountVectorizer(min_df=2)