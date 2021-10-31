from PyQt5 import QtWidgets, uic
from random import choice
import string

janela = QtWidgets.QApplication([])
interface = uic.loadUi("Des_.ui")

def main():
    string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
    string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    string.digits # 0123456789
    string.punctuation # <=>?@[\]^_`{|}~.

    tamanho = 15
    valores = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)


    interface.lineEdit.setText(senha)

def clear():
    interface.lineEdit.setText("")
    
interface.lineEdit.setReadOnly(True) 
interface.pushButton.clicked.connect(main)
interface.pushButton_2.clicked.connect(clear)
interface.show()
janela.exec()
