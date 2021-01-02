print("################################################################################") 
print('''
SUBSTITUTION PRINCIPLE\n''')
print("################################################################################") 

print('''
When subclassing is used to define a type hierachy, the subclass should be 
thought of as extending the behavior of their superclasses. We do this by adding
new attributes or overriding attributes inherited from a super class. For
example, TransferStudent extends Student by introducing a former school. 
Sometimes, the subclass overrides methods from the superclass, but this must be
done with care. In particular, important behaviors of the supertype must be
supported by each of its subtypes. If client code works correctly using an
instance of the supertype, it should also work correctly when an instance of the
subtype is substituted for the instance of the supertype. For example, it should
be possible to write client code using the specification of Student and have it
work correctly on a TransferStudent.
Conversely, there is not reason to expect that code written to work for
TransferStudent should work for arbitrary types of Student. \n''')
