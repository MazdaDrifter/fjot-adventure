class ReaderComponent:
    def __init__(self, filePath):
        self.filePath = filePath 
    def output(self):
        ff = open(self.filePath, 'r')
        # Print whats inside the file.
        print(ff.read())