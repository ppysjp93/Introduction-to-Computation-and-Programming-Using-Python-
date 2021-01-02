print("################################################################################") 
print('''
MORTGAGES, AN EXTENDED EXAMPLE\n''')
print("################################################################################") 

print('''
A collapse in U.S. housing prices helped trigger a severe economic meltdown 
in the fall of 2008. One of the contribting factors was that many homeoners had
taken on mortgages that ended up having unexpected consequences. 
In the beginning, mortgages were relatively simple beasts. One borrowed money
from a bank and made a fixed-size payment each month for the life of the
mortgage, which typically ranged from fifteen to thirty years. At the end of
that period, the bank had been paid back the intiial loan (the principal) plus
interest, and the homeowner owned the house "free and clear."
Towards the end of the twentieth century, mortgages started getting  a lot more
complicated. People could get lower interest rates by paying "points" to the
lender at the time they took on the mortgage. A point is a cash payment of 1% of
the value of the loan. People could take mortgages that were "interest only" for
a period of time.  That is to say, for some number of months at the start of the
loan the borrrower paid only the accrude interest and none of the principal.
Other loans involved multiple rates. Typically the intial rate (called a "teaser
rate") was low, and then it went up over time. Many of these loans were
variable-rate--the rate to be paid after the initial period would vary depending
upon some index intended to reflect the cost to the lender of borrowing on the
wholesale credit market. 
In principle, giving consumers a variety of options is a good thing. However,
unscrupulous loan purveyors were not always careful to fully explain the
possible long-term implications of the various options, and some borrowers made
choices that proved to have dire consequences.
Let's build a program that examines the costs of three kinds of loans.

    * A fixed-rate mortgage with no points
    * A fixed-rate mortgage with points, and
    * A mortgage with an initial teaser rate followed by a higher rate for the
      duration\n
''')

print('''
The point of this exercise is to provide some experience in the incremental
development of a set of related classes, not to make you an expert at mortgages.
We will structure our code to include a Mortgage class, and subclasses
corresponding to each of the three kinds of mortgages listed above. We first
create the abstract class Mortgage. This class contains methods that are shared
by each of its subclasses, but it is not intended to be instantiated directly.
That is no objects of type Mortgage will be created. 
The function findPayment at the top of the figure computes the size of the fixed
monthly payment needed to pay off the loan, including interest, by the end of
its term. It does this using a well-known closed-form expression. This
expression is not hard to derive, but it is a lot easier to just look it up and
more likely to be correct than one derived on the spot. 
Keep in mind that not everything you discover on the Web (or even in textbooks)
is correct. When your code incorporates a formula that you have looked up, make
sure that:

    * You have taken the formula from a reputable source. We looked at multiple
      reputable sources, all of which contained equivalent formulas.
    * You fully understand the meaning of all the variables in the formula
    * You test your implementation against examples taken from reputable sources.
      After implementing this function, we tested it by comparing our results to the
      results supplied by a calculator availble on the Web. \n''')

print('''
Looking at __init__, we see that all Mortgage instances will have instance
variables corresponding to the intitial loan amount, the monthly interest rate,
the duration of the loan in months, a list of payments that have been made at
the start of each month (the list starts with 0.0, since no payments have been
made at the start of the first month), a list with the balance of the
loan that is outstanding at the start of each month, the amount of money to be
paid each month (initialize using the value returned by the function
findPayment), and a description of the mortgage (which intially has a
value of None). The __init__ operation of each subclass of Mortgage is expected 
to start by calling Mortgage. __init__, and then to intiialize self.legend to an 
appropriate description of that subclass.\n''')


print('''
The method makePayment is used to record mortgage payments. Part of each payment
covers the amount of interest due on the outstanding loan balance, and the
remainder of the payment is used to reduce the loan balance. That is why
makePayment updates both self.paid and self.outstanding.
The method getTotalPaid uses the built-in Python function sum, which returns the
sum of a sequence of numbers. If the sequence contains a non-number  an
exception is raised.\n''')

print('''
Three non-abstract classes are implemented in Mortgage.py, FixedMortgage, 
FixedWithPts and TwoRate. The classes Fixed and FixedWithPts override __init__ 
and inherit the other three methods from Mortgage. The class TwoRate treats a 
mortgage as the concatenation of the two loans, each at a different interest rate. 
(Since self.paid is initialized to a list with one element, it contains one 
more element that the number of payments that have been made. That's why the 
method makepayment compares len(self.paid) to self.teaserMonths + 1.)\n''')

