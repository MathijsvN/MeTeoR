from abc import ABC, abstractmethod

class AbstractLiteral(ABC) :
    """
    AbstractLiteral class is for denoting an object of class Atom or OperatorLiteral.
    e.g.,  A(mike), Boxminus[1,2]Professor(X) or B(jane)Until[2,5]C(mike)
    """

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __hash__(self):
        pass