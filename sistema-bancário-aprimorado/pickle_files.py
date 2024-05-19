import os
import pickle

script_path = os.path.dirname(os.path.abspath(__file__))  
contas_path = os.path.join(script_path, 'contas.pickle')
usuarios_path = os.path.join(script_path, 'usuarios.pickle')
contas, usuarios = {}, []

def writeUsuarios(usuarios):
    with open(usuarios_path, 'wb') as USUARIOS:
        pickle.dump(usuarios, USUARIOS)

def writeContas(contas):
    with open(contas_path, 'wb') as CONTAS:
        pickle.dump(contas, CONTAS)

def readUsuarios(usuarios):
    with open(usuarios_path, 'rb') as USUARIOS:
        usuarios = pickle.load(USUARIOS)
    return usuarios

def readContas(contas):
    with open(contas_path, 'rb') as CONTAS:
        contas = pickle.load(CONTAS)
    return contas