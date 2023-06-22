# Parkinson-s-Disease-Prediction

Parkinson's disease prediction using MRI scan, Spiral image and Voice data, with neural network and website deployment with django.

## Introduction

-> Parkinson's disease is a neurodegenerative disorder that affects movement. 
-> It is caused by the degeneration of dopamine-producing neurons in a region of the brain called the substantia nigra, which is responsible for controlling movement. 
-> As a result, people with Parkinson's disease may experience a wide range of symptoms, including tremors, stiffness, slowness of movement, and difficulty with balance and 
   coordination.
-> Parkinson's disease is caused over the age of 50, but it can occur in younger individuals as well.
-> There is currently no cure for Parkinson's disease, but treatments are available to help manage symptoms and improve quality of life.
-> These may include medications, such as levodopa and dopamine agonists, as well as physical therapy and deep brain stimulation.

## Objective

The development of a deep learning model for Parkinson's disease diagnosis using MRI scans, spiral image and voice signal can have several benefits. 
-> It can help improve the accuracy and efficiency of diagnosis, which can lead to earlier detection and treatment of the disease.
-> It can provide valuable insights into the underlying biology of the disease and help identify new targets for treatment. 
-> It can facilitate the development of personalized treatment plans for patients with Parkinson's disease

## Architecture

<img width="480" alt="image" src="https://github.com/aneesh1308/Parkinson-s-Disease-Prediction/assets/82936701/8138a18c-04d1-433d-b0fe-4c900b96da90">

## Modules Description

Deep Learning Model Building:
	Convolutional and pooling layers are often followed by fully linked layers in a model. Twenty layers and nodes altogether are adjusted. then the model is compiled by specifying the metrics "accuracy," the optimizer "adam," and the loss function "binary crossentropy." 500 epochs of iteration over the training data are used in the training procedure with early stopping.

Machine Learning Model Building:
	The XGBoost model is trained on the extracted features using labeled data, with Parkinson's disease status as the target variable. The model is then tested on a separate dataset to evaluate its performance.The XGBoost model is a machine learning algorithm that can be used to predict PD based on voice data. To train an XGBoost model for PD prediction we use various features extracted from the voice signals, such as pitch, frequency, jitter, etc. The XGBoost algorithm uses gradient boosting to create an ensemble of decision trees that can accurately classify the voice data.(accuracy - 94)

Sequential Model Building For Tremors (CNN):
	Convolutional and pooling layers are often followed by fully linked layers in a model. Twenty layers and nodes altogether are adjusted. then the model is compiled by specifying the metrics "accuracy," the optimizer "rmsprop" and the loss function "binary crossentropy." 200 epochs of iteration over the training data are used in the training procedure with early stopping.For Parkinson’s Disease prediction using MRI scans we used a model of deep learning called sequential model with 20 layers of convolutional neural network. The model can then learn to identify patterns in the data that are associated with Parkinson's disease.(accuracy – 92% for MRI Model) & (accuracy – 94% for Tremors Model)

Deployment:
	Front-End Development: The front-end of the web application is developed using HTML, CSS, and JavaScript. 
	Back-End Development: The back-end of the web application is developed using a web framework, such as Django or Flask. This includes creating a server, connecting 
                              to a database, and integrating the neural network model.
	Model Integration: The trained neural network model is integrated into the web application by creating an API that allows users to input MRI scans and receive predictions.

<img width="667" alt="image" src="https://github.com/aneesh1308/Parkinson-s-Disease-Prediction/assets/82936701/34204811-0e2f-4595-9bb1-32a667e36bcf">

<img width="750" alt="image" src="https://github.com/aneesh1308/Parkinson-s-Disease-Prediction/assets/82936701/f82ec878-70b3-485c-943d-141f4f575f05">

<img width="844" alt="image" src="https://github.com/aneesh1308/Parkinson-s-Disease-Prediction/assets/82936701/55c20555-c962-4c90-b249-5ccfc0795594">

## Conclusion

-> The project focuses on predicting Parkinson's disease using MRI scan and deep learning algorithms.
-> The results show promising accuracy in predicting Parkinson's disease using MRI imaging data and deep learning.
-> Early diagnosis and treatment of Parkinson's disease could be improved with this technology, leading to better patient outcomes.
-> Further research is needed to validate the accuracy and generalizability of the model in different populations and settings.
-> The project demonstrates the potential of using advanced machine learning techniques for medical diagnosis and treatment





