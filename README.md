# pydeploy
Deploying a python model with Docker

## Docker commands
Docker build -t pythonmod:v1

Docker run -p 5000:5000 pythonmod:v1

## Postman
1. Check if its working

GET request http://localhost:5000 should return "working"

2. Score the model on data in real time

POST request to Url http://localhost:5000/predict


Use json body:

{
  "crim": 0.00632,
  "zn": 18.0,
  "indus": 2.31,
  "chas": 0,
  "nox": 0.538,
  "rm": 6.575,
  "age": 65.2,
  "dis": 4.0900,
  "rad": 1,
  "tax": 296,
  "ptratio": 10.3,
  "b": 396.90,
  "lstat": 4.98
}
