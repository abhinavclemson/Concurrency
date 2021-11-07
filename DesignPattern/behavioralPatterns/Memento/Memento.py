from unittest import *
from copy import deepcopy


class Token:
    def __init__(self, value=0):
        self.value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


class TokenLog:
    def __init__(self):
        self.__states = [""]

    def get_state(self):
        return self.__states.pop()

    def set_state(self, token):
        self.__states.append(token)

    def last_state(self):
        if len(self.__states)>0:
            return self.__states[-1]


class TokenMachine:
    def __init__(self):
        self.__token_log = TokenLog()
        self.__mememto = Token()


    def add_token(self, value):

        #adding existing mememto into tokens list
        if self.__mememto.get_value() is not None:
            self.__token_log.set_state(self.__memento)

        #updating mememto
        self.__mememto = Token(value)


    def revert(self, memento):

        if len(self.__token_log)>0:
            self.__mememto = self.__token_log.get_state()
            return "Success!"

        return "Cannot Undo: Unable to find Previous token"




