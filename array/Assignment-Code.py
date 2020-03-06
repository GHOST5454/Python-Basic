import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.linear_model.tests.test_logistic import test_logistic_cv_mock_scorer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap

data = pd.read_csv('corier data.csv')

real_x = data.iloc[:, [1, 2, 3]].values
real_y = data.iloc[:, 4].values

traning_x, test_x, traning_y, test_y = train_test_split(real_x, real_y, test_size=0.25, random_state=0)
Scaler = StandardScaler()
traning_x = Scaler.fit_transform(traning_x)
test_x = Scaler.fit_transform(test_x)

cls_svc = svm.SVC(kernel='linear', random_state=0)
cls_svc.fit(traning_x, traning_y)

y_pred = cls_svc.predict(test_x)

x_set, y_set = traning_x, traning_y

x1, x2, x3 = np.meshgrid(np.arange(start=x_set[:, 0].min() - 1, stop=x_set[:, 0].max() + 1, step=0.01),
                         np.arange(start=x_set[:, 1].min() - 1, stop=x_set[:, 1].max() + 1, step=0.01),
                         np.arange(start=x_set[:, 2].min() - 1, stop=x_set[:, 2].max() + 1, step=0.01))
plt.contourf(x1, x2, cls_svc.predict(np.array([x1.ravel(), x2.ravel()]).T).shape(x1.shape),
             alpha=0.75, cmap=ListedColormap(('red', 'green')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c=ListedColormap(('red', 'green'))(i), label=j)

plt.title('SVM(Training set)')
plt.xlabel('distance')
plt.ylabel('status')
plt.legend()
plt.show()

