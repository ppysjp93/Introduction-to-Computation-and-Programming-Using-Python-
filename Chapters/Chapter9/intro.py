print("################################################################################") 
print('''
ALGORITHMIC COMPLEXITY\n''')
print("################################################################################") 

print('''
The most important thing to think about when designing and implementing a 
program is that it should produce results that can be relied upon. We want our
bank balances to be calculated correctly. We want the fuel injectors in our
autmobiles to inject appropriate amounts of fuel. We would prefer that neither
airplanes nor operating systems crash. Sometimes perfomance is an important
aspect of correctness.
This is most obvious for programs that need to run in real time. A program that
warns airplanes of potential obstructions needs to issue the warning before the
obstructions are encountered. Performance can also affect the utility of many
non-real-time programs. The number of transactions completed per minute is an
important metric when evaluating the utility of database systems. Users care
about the time required to start an application on their phone. Biologists care
about how long their phylogenetic inference claculations take. Writing efficient
programs isnot easy. The most straightforward solution is often not the most
efficient. 
Computationally efficient algorithms often employ subtle tricks that can make
them difficult to understand. Consequently, programmers often increase the
conceptual complexity of a program in an effort to 5educe its computational
complexity. To do this in a sensible way, we need to understand how to go about
estimating the computational complexity of a program. That is the topic of this
chapter.\n''')
