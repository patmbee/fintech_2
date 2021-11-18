# Module 10 Challenge
## Crypto Clustering
Machine learning is a type of artificial intelligence that uses algorithms and statistical models to make decisions or predictions about data. 

This project focuses on unsupervised learning one of the three main branches of machine learning. With unsupervised learning, the algorithm tries to make sense of an unlabeled dataset by extracting features and patterns on its own.

Specifically in this project algorithms were applied to a cryptocurrencies dataset to find the:

* best value for k
* cluster with K-means 
* optimize clusters with Principal Component Analysis
* find best value for k using PCA
* cluster currencies with K-means using PCA data
* pandas hvplot is used to plot the data

Images contrast the Elbow Curve created to find the best value for k with the original and the PCA data.

![alt text](
./Resources/image1.png)

Scatter plot comparison of original data set and one using fewer features
![alt text](
./Resources/image2.png)

- - - 

## Technologies
### Libraries

The project was buildt using Python 3.7 and several python libraries listed below in a code block. 


Import the following dependencies
###  Modules
```
import pandas as pd
import hvplot.pandas
from path import Path
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
```



### 
- - - 
## Installation Guide
If you need help with installing Python 3.7 please use this link to Python guides.

[Python documentation](https://docs.python.org/3.7/)



- - - 
## Contributors
This is a student project 


- - - 
## License
Any usage of this app should be authorized from Columbia Univesity bookcamp.


