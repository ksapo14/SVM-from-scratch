#%%
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

#%%
iris = load_iris()
X = iris.data
y = (iris.target > 0).astype(int)
# %%
plt.plot(X[y==0, 0], X[y==0, 1], 'b.')
plt.plot(X[y==1, 0], X[y==1, 1], 'r.')
# %%
def rbf_kernel(X1, X2, gamma=1):
    pass