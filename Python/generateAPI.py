from asyncio.windows_events import NULL
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class getData(Resource):
    def get(self, strTitre=NULL):
        if strTitre == NULL:
            return random.choice(ai_quotes), 200
        for quote in ai_quotes:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404