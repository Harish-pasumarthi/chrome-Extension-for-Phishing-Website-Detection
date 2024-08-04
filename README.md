# chrome-Extension-for-Phishing-Website-Detection

This Chrome extension is designed to identify and block phishing websites in real-time, leveraging the Random Forest algorithm for accurate detection. The extension enhances online security by protecting users from malicious websites.

## Table of Contents

- [Abstract](#abstract)
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Project Objective](#project-objective)
- [Scope and Limitations](#scope-and-limitations)
- [Existing Solutions](#existing-solutions)
- [Proposed Solution](#proposed-solution)
- [System Requirements and Tools](#system-requirements-and-tools)
- [Results and Discussion](#results-and-discussion)
- [Conclusion](#conclusion)

## Abstract

In today's digital world, phishing is a significant cyber threat where attackers use fraudulent websites to trick users into sharing sensitive information. This Chrome extension aims to combat phishing by identifying and blocking such websites in real-time using machine learning algorithms.

## Introduction

Phishing websites are designed to deceive users into revealing sensitive information like usernames, passwords, and credit card numbers. Detecting and blocking these websites is crucial for online security. This project employs machine learning techniques to develop an effective Chrome extension for phishing detection.

## Problem Statement

The rise in internet usage has led to an increase in phishing attacks. Traditional detection methods often fail to keep up with the evolving tactics of cybercriminals. There is a need for a robust, user-friendly solution to protect users from these malicious sites.

## Project Objective

The objective is to develop a Chrome extension that uses machine learning algorithms to detect and block phishing websites in real-time. The extension will provide a seamless user experience while ensuring robust protection against phishing attacks.

## Scope and Limitations

### Scope
- **Machine Learning Integration:** Implement advanced machine learning algorithms to analyze URL patterns and website features.
- **User-Friendly Interface:** Create an intuitive interface with clear notifications and alerts.

### Limitations
- False positives/negatives
- Resource intensive
- Adaptation lag
- Browser compatibility

## Existing Solutions

- **Browser-Based Security Features:** Built-in phishing protection in modern web browsers.
- **Email Filtering:** Sophisticated algorithms to filter out phishing emails.
- **Third-Party Security Software:** Comprehensive protection against phishing from antivirus programs.
- **Web of Trust (WOT):** Community-based tools for rating and reviewing websites.
- **Two-Factor Authentication (2FA):** Extra security layer for online accounts.
- **Phishing Awareness Programs:** Education and training to recognize phishing attempts.
- **Phishing Detection APIs:** Real-time protection by flagging suspicious websites.
- **Content Filtering and Network Security Appliances:** Devices to filter web traffic and block malicious sites.

## Proposed Solution

### Machine Learning-Based Chrome Extension
This extension uses the Random Forest algorithm to detect and block phishing websites by analyzing URL features and web content. The algorithm's ensemble learning approach enhances classification accuracy and reduces overfitting.

## System Requirements and Tools

### Hardware Components
- Processor: AMD Ryzen 9 7940HS w/ Radeon 780M Graphics 4.00 GHz
- RAM: 64.0 GB

### Software Tools and Versions Used
- **Operating System:** Windows, macOS, or Linux
- **Browser:** Google Chrome (Version 90 or higher)
- **Extension Framework:** Chrome Extension SDK (manifest v3)
- **Database:** Local storage for phishing site data
- **Programming Languages:** HTML, CSS, JavaScript, Python
- **Python Libraries:** pandas, scikit-learn, joblib, flask, numpy

### Network and Other Dependencies
- **Internet Connection:** Required for downloading software and libraries and receiving updates.

## Results and Discussion

The Chrome extension effectively detects and blocks phishing websites. Users receive notifications when encountering potential phishing sites, enhancing their online safety. The integration of the Random Forest algorithm ensures robust and accurate detection.

## Conclusion

The implementation of the Random Forest algorithm in the Chrome extension has proven to be an effective solution for phishing detection. The extension provides real-time alerts to users, reducing the risk of falling victim to phishing attacks. This project demonstrates the potential of machine learning in cybersecurity and contributes to a safer online experience.

## Python Code for Phishing Detection

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
dataset = pd.read_csv('Phishing_Legitimate_full.csv')

# Split the dataset into features and labels
X = dataset.drop("CLASS_LABEL", axis=1)
y = dataset["CLASS_LABEL"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "random_forest_model.pkl")

print("Model trained and saved successfully.")
