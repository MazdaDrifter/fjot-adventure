def reader(filePath):
    f = open(filePath, 'r')
    operators = ['@', '$'] #// $ is an operator to declare it is a var.
    