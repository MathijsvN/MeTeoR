from meteor_reasoner.classes_new.classes_literal.operator_literal import OperatorLiteral
from meteor_reasoner.classes_new.classes_literal.abstract_literal import AbstractLiteral
from meteor_reasoner.classes_new.operator import Operator

class UnaryLiteral(OperatorLiteral):
    """
    Literal class is for storing a literal consisting of one atom with one or multiple MTL operators,
    e.g., Boxminus[1,2]Professor(X)
    """
    def __init__(self, literal : AbstractLiteral, operator : Operator):
        """
        
        Args:
            literal (AbstractLiteral class):
            operator (Operator class):
        """
        self.literal = literal
        self.operator = operator

    def get_op_name(self):
        return self.operator.name

    def __eq__(self, other):
        if isinstance(other, UnaryLiteral):
            if self.literal == other.literal and self.operator == other.operator:
                return True
        return False

    def __str__(self):
        return "".join(str(self.operator) + str(self.literal))

    def __hash__(self):
        hash_value = hash("UnaryLiteral" + str(self.atom) + str(self.operator))
        return  hash_value
