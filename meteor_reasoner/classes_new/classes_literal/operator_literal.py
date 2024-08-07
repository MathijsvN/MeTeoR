from abc import ABC, abstractmethod
from meteor_reasoner.classes_new.classes_literal.abstract_literal import AbstractLiteral

class OperatorLiteral(ABC, AbstractLiteral) :
    """
    OperatorLiteral class is for storing a literal consisting of one or multiple MTL operators,
    e.g., Boxminus[1,2]Professor(X), Boxplus[0,10]{{Diamondplus[1,2]A(mike)}Since[0,1]B(mike)}
    """

    @abstractmethod
    def get_operator(self) :
        pass