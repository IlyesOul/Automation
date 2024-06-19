import math
import statistics as stats

# Class of useful math functions that I find redundant
class MathSimplifier:

    # Simplifying fractions
    def simply_fraction(self, numerator, denominator):

        # Basic conditions
        if numerator%denominator == 0:
            return numerator/denominator, 1
        elif denominator%numerator == 0:
            return 1, denominator/numerator

        # Retrieve Greatest Common Factor between numbers
        gcf = self.GCF(numerator, denominator, denominator)

        return numerator/gcf, denominator/gcf

    # Recursively returns GCF between two numbers
    def GCF(self, n1, n2, index):
        if n2 >= 0:
            if n1%index == 0 and n2%index ==0:
                return index
            return self.GCF(n1, n2, index-1)
        else:
            return 0

# Testing functions
simplifier_class = MathSimplifier()
print(f"72/20 simplified is {simplifier_class.simply_fraction(72,20)}")