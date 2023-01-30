# Delivery fee calculator <!-- API omit in toc -->
1. [Why Flask? Django vs Flask](#django-vs-flask)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [Deployment](#deployment)
5. [Tests](#tests)
## Django vs Flask

To decide whether I will use Flask or Django as a Framework to develop this API, first I have to make clear the requirements and information I have about the project. 

The project consists on implementing a **single endpoint API** which will recieve a request with a JSON payload containing the information about a shopping cart, and will return a response with a JSON payload containing the delivery fee of that shopping cart.

With this in mind and no prior context on how the structure of the rest of the e-commerce platform might be, I can evaluate wich framework suits best this situation.




| Flask                                                     | Django                         |
| ----------------------------------------------------------|--------------------------------|
| Micro-Framework                                           | Full-Stack Framework           |
| Un-opinionated Framework                                  | Opinionated Framework          |
| Very lightweight and fast                                 | Larger default extension       |
| Distributed architecture, oriented to microservices       | Monolithic architecture        |
| Doesn´t rely on external libraries but has extensions     | Heavily reliant on libraries   |
| MVC framework                                             | Free choice                    |
| Less documented                                        | Extensive documentation        |



This is a simple application with just one endpoint in one server, there is no persistence of data in databases and I don´t have a clear view of the project´s architecture (monolithic or distributed) but distributed systems and microservices are a current trend that is being widely adopted. Calculating the delivery fee could be deployed as a microservice wich would make it easier to mantain, although the general structure would be more complex. It would also be easier to test, deploy and as it is a small service, easier to understand for developers. With all this in mind, I choose to use flask.





## Project Structure

```
├── app
│   ├── app.py --> Flask project creation and API routing declaration
│   └── api
│       ├── models    --> Pydantic models used to validate and serialize/deserialize data
│       ├── resources --> Flask-restful Resources used to act upon an upcoming HTTP request
│       └── services  --> Functions accesed by Resources to operate with data
│
├── test
│   ├── conftest.py
│   ├── integration
│   │   └── resources
│   └── unit
│       ├── models
│       └── services
│
├── .flaskenv
├── README.md
└── requirements.txt
```







## Requirements

- Python 3.11
- pip 22.3.1

To install all the dependencies move to project root and execute the following
```bash
> pip install -r requirements.txt
```

## Deployment
To launch the Flask project use
```bash
> flask run
```
Project hosted on http://127.0.0.1:5000

Send post requests to http://127.0.0.1:5000/api/calculate-delivery-fee

Post body format
```python
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
```
Response format
```python
{"delivery_fee": 710}
```

## Tests
To launch all the tests with coverage
```bash 
> coverage run -m pytest
```
```
collected 30 items                             
test\integration\resources\test_delivery_fee_resource.py ....            [ 13%]
test\unit\models\test_cart_model.py .......                              [ 36%]
test\unit\models\test_delivery_fee_model.py .....                        [ 53%]
test\unit\services\test_calculate_fee_service.py .....                   [100%]
=============================== 30 passed in 0.19s ============================
```
To see coverage results
```bash
> coverage report -m
```
```
Name                                                       Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------------------
app\__init__.py                                                0      0   100%
app\api\__init__.py                                            0      0   100%
app\api\models\__init__.py                                     0      0   100%
app\api\models\cart_model.py                                  12      0   100%
app\api\models\delivery_fee_model.py                           8      0   100%
app\api\resources\__init__.py                                  0      0   100%
app\api\resources\delivery_fee_resource.py                    17      0   100%
app\api\services\__init__.py                                   0      0   100%
app\api\services\calculate_fee_service.py                     18      0   100%
app\app.py                                                     8      0   100%
test\__init__.py                                               0      0   100%
test\conftest.py                                               8      0   100%
test\integration\resources\test_delivery_fee_resource.py      19      0   100%
test\unit\__init__.py                                          0      0   100%
test\unit\models\__init__.py                                   0      0   100%
test\unit\models\test_cart_model.py                           28      0   100%
test\unit\models\test_delivery_fee_model.py                   16      0   100%
test\unit\services\__init__.py                                 0      0   100%
test\unit\services\test_calculate_fee_service.py               9      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                        143      0   100%
```
