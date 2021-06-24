from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score 

import pickle
from final_data import X_train, X_test, Y_train, Y_test

#Artificial Neural Networks (MLP)
from sklearn.neural_network import MLPClassifier
MLP = MLPClassifier(random_state=0, max_iter=600).fit(X_train, Y_train)
Y_pred = MLP.predict(X_test)


#save model
filename = 'finalized_model.sav'
pickle.dump(MLP, open(filename, 'wb'))

#Evaluation
cm = confusion_matrix(Y_test, Y_pred)
print("\nMLP")
print('Confusion Matrix: \n' , cm)
print(classification_report(Y_test,Y_pred))
print('Accuracy: ', accuracy_score(Y_test, Y_pred)*100)
print('Precision: ' , precision_score(Y_test, Y_pred)*100)
print('Recall: ', recall_score(Y_test, Y_pred)*100)
print('F-score: ' ,(f1_score(Y_test, Y_pred)*100))

#to save trained model
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
