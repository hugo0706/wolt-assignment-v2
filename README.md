# Delivery fee calculator <!-- API omit in toc -->
1. [Why Flask? Django vs Flask](#django-vs-flask)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
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


## Requirements
python

Create a python virtual environment
On Windows:
```bash 
> mkdir assignment
> cd assignment
> py -3 -m venv venv
#Activate virtual environment
> .\venv\Scripts\activate
```

On MacOs/Linux:
```bash 
$ mkdir assignment
$ cd assignment
$ python3 -m venv venv
#Activate virtual environment
$ . venv/bin/activate
```

Install Flask on your venv
- Werkzeug 
- Jinja 
- MarkupSafe
- ItsDangerous
- Click 

Python 3.11.1
Flask 2.2.2
Werkzeug 2.2.2
python-dotenv
flask-restful
pip install -U marshmallow
```bash

```

## Deployment

recomend virtual env