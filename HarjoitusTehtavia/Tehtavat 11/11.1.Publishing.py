class Publishing:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Name: {self.name}")

class Book(Publishing):
    def __init__(self, name, writer, pages):
        self.writer = writer
        self.pages = pages
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Writer: {self.writer}\nPages: {self.pages}")

class Magazine(Publishing):
    def __init__(self,name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Editor-In-Chief: {self.editor}")

publishings = []
publishings.append(Magazine("Aku Ankka","Aki Hyyppä"))
publishings.append(Book("Hytti n:o 6", "Rosa Liksom", 200))

for pub in publishings:
    pub.print_info()
    print("---")