from flask_restful import Resource
from http import HTTPStatus
from flask import request
from .models import Pessoa

class PessoaListResource(Resource):
    def get(self):
        try:
            data = [pessoa.data for pessoa in Pessoa.query.all()]

            return {'data': data}, HTTPStatus.OK
        except Exception as ex:
            return {'message': '500 Interval Server Error'}, HTTPStatus.INTERNAL_SERVER_ERROR
    
    def post(self):
        try:
            nome = request.form['nome']
            rg = request.form['rg']
            cpf = request.form['cpf']
            data_nascimento = request.form['data_nascimento']
            data_admissao = request.form['data_admissao']
            funcao = request.form['funcao']

            pessoa = Pessoa(nome=nome, rg=rg, cpf=cpf, data_nascimento=data_nascimento, data_admissao=data_admissao, funcao=funcao)
            pessoa.save()

            return pessoa.data, HTTPStatus.CREATED
        except Exception as ex:
            return {'message': '500 Interval Server Error'}, HTTPStatus.INTERNAL_SERVER_ERROR



class PessoaResource(Resource):
    def get(self, pessoa_id: int):
        pessoa = Pessoa.query.get(pessoa_id)

        if pessoa is None:
            return {'message': '404 Not Found'}, HTTPStatus.NOT_FOUND
        
        return pessoa.data, HTTPStatus.OK
    
    def put(self, pessoa_id: int):
        pessoa = Pessoa.query.get(pessoa_id)

        if pessoa is None:
            return {'message': '404 Not Found'}, HTTPStatus.NOT_FOUND

        try:
            pessoa.nome = request.form['nome']
            pessoa.rg = request.form['rg']
            pessoa.cpf = request.form['cpf']
            pessoa.data_nascimento = request.form['data_nascimento']
            pessoa.data_admissao = request.form['data_admissao']
            pessoa.funcao = request.form['funcao']
            pessoa.save()

            return pessoa.data, HTTPStatus.OK
        except Exception as ex:
            return {'message': '500 Interval Server Error'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def delete(self, pessoa_id: int):
        pessoa = Pessoa.query.get(pessoa_id)

        if pessoa is None:
            return {'message': '404 Not Found'}, HTTPStatus.NOT_FOUND

        try:
            pessoa.delete()

            return {}, HTTPStatus.NO_CONTENT
        except Exception as ex:
            return {'message': '500 Interval Server Error'}, HTTPStatus.INTERNAL_SERVER_ERROR