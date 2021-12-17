# Module 13 Challenge
## Venture Funding with Deep Learning
This is a Deep Machine Learning project developed to evaluate venture capital start ups.
We have created a model that predicts whether applicants will be successful after projected funding.

The raw data is CSV containing more than 34,000 organizations that have received funding from our team over the years. The project utilizes the features in the provided dataset to create a binary classifier model that will predict whether an applicant will become a successful business. The CSV file contains a variety of information about these businesses, including whether or not they ultimately became successful.

Main project with first three models is named 'venture_funding_with_deep_learning.ipynb'. Second file named venture_funding_with_deep_learning_dropFeatures.ipynb contains a single model with fewer features.

All models are saved in the Resources folder. 


## Steps taken in Project
* Prepare the data for use on a neural network model.

* Compile and evaluate a binary classification model using a neural network.

* Optimize the neural network model.

## Deep Learning Results
The project contains the results of the original model and four 'optimized' models. The top accuracy score is 73% (Alternate model 3). All of the models have been saved to an h5 file located in the Resoures folder.

Accuracy Scores
Original Model - 72.89%
Alt Model 1 - 72.99%
Alt Model 2 - 72.89%
Alt Model 3 - 73%

the loss was consistent across all models at 55% except Alt Model 3 which had a slighly higher loss of 56% offsetting the increase in accuracy of 1%. 

The key difference between the models is the change in inputs, layers and epochs. Various inputs were eliminated while training alt model 3 with a worsening accuracy. 

- - - 

## Technologies
### Libraries

The project was buildt using Python 3.7 and several python libraries listed below in a code block. 

###  Modules
```
# Imports
import pandas as pd
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
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
Any usage of this app should be authorized from Columbia Univesity bootcamp.