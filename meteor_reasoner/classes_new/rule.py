from meteor_reasoner.classes_new.classes_literal.atom import Atom
from meteor_reasoner.classes_new.classes_literal.abstract_literal import AbstractLiteral
from meteor_reasoner.classes_new.classes_literal.unary_literal import UnaryLiteral

class Rule:
    """
    A rule instance consists of two part: a head and
    a body. 
    The head is an instance of class Atom or of class UnaryOperator, where the Operator is Boxplus or Boxminus.
    The body is a list of AbstractLiteral instances.
    """


    def __init__(self, head: AbstractLiteral, body: list = [], negative_body: list =[]):
        """

        Args:
            head (an instance of class Atom or of class UnaryOperator, where the Operator is Boxplus or Boxminus):
            body (a list of AbstractLiteral instances):
            negative_body (a list of AbstractLiteral instances):
        """
        if isinstance(head, Atom) or ( isinstance(head, UnaryLiteral) and head.get_op_name().name in ['Boxplus', 'Boxminus'] ) :
            self.head = head
        else :
            raise Exception("{} has an incorrect syntax!".format(head))
        if all( isinstance(lit, AbstractLiteral) for lit in body) :
            self.body = body
        else :
            raise Exception("{} has an incorrect syntax!".format(body))
        if all( isinstance(lit, AbstractLiteral) for lit in negative_body ) :
            self.negative_body = negative_body 
        else:
            raise Exception("{} has an incorrect syntax!".format(negative_body))


    def __str__(self):
        if len(self.negative_body) == 0:
            return str(self.head) + ":-" + ",".join([str(literal) for literal in self.body])
        else:
            return str(self.head) + ":-" + ",".join([str(literal) for literal in self.body])\
                   + "||" + ",".join([str(literal) for literal in self.negative_body_atoms])