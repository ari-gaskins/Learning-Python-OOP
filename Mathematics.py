# example of static methods

class Mathematics:
    
    # static methods can be created to be used in any situation as needed
    # simply through access of the class
    @staticmethod
    def add5(x):
        return(x + 5)

    # arguments are not required
    @staticmethod
    def pr():
        print('run')

print(Mathematics.add5(9))

Mathematics.pr()