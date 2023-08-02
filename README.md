# Phishing URL Detection

## Overview

This project aims to develop an ML model for detecting phishing URLs using the "PhishStorm" dataset. Phishing URLs are malicious links that mimic legitimate websites to deceive users and steal sensitive information. The model will help identify and block such URLs, enhancing cybersecurity measures.

## Dataset

The dataset used for training and evaluating the ML model is called "PhishStorm." It contains labeled URLs, where each URL is classified as either "phishing" or "legitimate." The dataset is available [here](https://ieeexplore.ieee.org/document/6975177).

## Model Training
Before model training the dataset needed some preprocessing. The data is preprocessed to extract relevant features, and a machine learning algorithm (Random Forest) is trained on this processed data to predict whether a given URL is a phishing URL or not. The model achieved 90% accuracy.

## Webpage Demonstration

To provide a user-friendly interface for URL classification, a webpage is created. The webpage allows users to input a URL, and the ML model will classify it as either phishing or legitimate. The webpage also displays the confidence score and the reasoning behind the classification decision.

![Webpage Screenshot](https://github.com/Anam-jafar/Phishing-URL-Detection/blob/main/Screenshots/Landing%20Page.png))

## Usage

To use the model and webpage, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Run the Django application to start the webpage.
4. Enter a URL in the input box and click "Classify."
5. The webpage will display the classification result.



