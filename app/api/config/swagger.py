template = {
    "swagger": "2.0",
    "info": {
        "title": "Cart delivery fee calculator",
        "description": "Api that calculates the delivery fee for a shopping cart",
        "version": "1.0.0",
        "contact": {
            "name": "Hugo Garcia",
            "email": "hugo.garciac@edu.uah.es"
        }
    },
    "basePath": "/api",
    "schemes": [
        "http"
    ]
}

swagger_config = {
    "headers": [

    ],
    "specs": [{
        "endpoint": "swagger",
        "route": "/swagger.json",
        "rule_filter": lambda rule: True,
        "model_filter": lambda tag: True
    }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}
