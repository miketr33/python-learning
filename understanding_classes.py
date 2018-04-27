class StartClass():
    def __init__(self):
        self.create_lists()

    def create_lists(self):
        self.list_from_start_class = []
        self.list_2_from_start_class = []
        global list_from_start_class
        global list_2_from_start_class

    def get_lists(self):
        return self.list_from_start_class, self.list_2_from_start_class

class AlterationsClass():
    def __init__(self):
        self.result = StartClass.get_lists(self)
        print("Retrieved list: " + str(self.result))

class ReadListClass():
    def __init__(self):
        self.received_list = StartClass.create_lists(self)
        print(str(self.received_list))

StartClass()
AlterationsClass()
ReadListClass()
