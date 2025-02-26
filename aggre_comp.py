class Other:
    def __init__(self, string):
        self.string = string                                    

    def retrieve_string(self):
        return f'Hi from Other class {self.string} '


class Composition:
    def __init__(self, string):
        self.other_class = Other(string)

    def result(self):
        return self.other_class.retrieve_string() + ' world!'


composition = Composition('Hello')
print(composition.result())

