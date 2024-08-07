from meteor_reasoner.classes_new.classes_literal.operator_literal import OperatorLiteral
from meteor_reasoner.classes_new.classes_literal.abstract_literal import AbstractLiteral
from meteor_reasoner.classes_new.operator import Operator

class BinaryLiteral(OperatorLiteral):
    """
    The BinaryLiteral class is used to store binary literal, in which there are two literal separated by
    Until or Since Operator, e.g. A(X)Since[1,2]B(X,Y)
    """
    def __init__(self, left_literal : AbstractLiteral, right_literal : AbstractLiteral, operator : Operator):
        """

        Args:
            left_atom (AbstractLiteral class):
            right_atom (AbstractLiteral class):
            operator (Operator class):
        """
        self.left_literal = left_literal
        self.right_literal = right_literal
        self.operator = operator

    def get_op_name(self):
        return self.operator.name

    def __eq__(self, other):
        if isinstance(other, BinaryLiteral):
            return self.left_literal == other.left_literal and self.right_literal == other.right_literal and \
                   self.operator == other.operator
        return False

    def __str__(self):
        return str(self.left_literal) + str(self.operator) + str(self.right_literal)

    def __hash__(self):
        return hash("BiLiteral:" + str(self.left_literal) + str(self.operator) + str(self.right_literal))


