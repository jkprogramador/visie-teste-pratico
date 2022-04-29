from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    db.init_app(app)

    from app.resources import PessoaListResource, PessoaResource
    
    api= Api(app)
    api.add_resource(PessoaListResource, '/pessoas')
    api.add_resource(PessoaResource, '/pessoas/<int:pessoa_id>')

    @app.route('/')
    def home():
        return render_template('home.html')

    return app