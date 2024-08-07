from meteor_reasoner.classes_new.interval import Interval

class Operator:
    """
    The operator class is designed for storing six MTL operators, e.g., Boxminus[1,2],
    Boxplus(1,2), Diamondplus[3,4], Diamondminus[1,2], Since[1,2], Until[2,3]
    """
    def __init__(self, name : str, interval : Interval):
        """
        Args:
            name (str): Boxminus, Boxplus, Diamondplus, Diamondminus, Since, Until
            interval (Interval class):
        """
        if name not in ["Boxminus", "Boxplus", "Diamondplus", "Diamondminus", "Since", "Until"]:
            raise ValueError("Only support one of six operators (Boxminus, Boxplus, Diamondplus, "
                             "Diamondminus, Since, Until)!")

        self.name = name
        self.interval = interval

    def __eq__(self, other):
        if isinstance(other, Operator) and self.name == other.name and self.interval == other.interval:
            return True

        return False

    def __str__(self):
        return self.name + str(self.interval)
