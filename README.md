# Prototypes

This repository contains a minimalistic setup to enable rapid prototyping for technical demos. The focus here is not to achieve the optimum machine learning performance. The setup is organized to achieve a loose coupling between machine learning and model serving. It deliberately ignores some security best practises!

- In the directory 'BreastCancerPrediction_Python_Flask' I created a flask app to serve a simple decision tree model diagnosing breast cancer as a REST service (simply execute the python script 'app.py' or launch the app in docker via the shell script 'dockerLaunchFlaskApp.sh'). For transparency I have also included the dockerfile. The app listens on port 5000. A sample request script 'sampleRequest.py' can be used to invoke the service via CLI.

- In the directory 'BreastCancerPrediction_R_Plumber' I used plumber to expose a simple conditional inference tree based service via API (simply execute the 'app.R' script). The app listens on port 8000. The postman collection 'BreastCancerAnalysisViaR.postman_collection.json' can be used to test the service.
