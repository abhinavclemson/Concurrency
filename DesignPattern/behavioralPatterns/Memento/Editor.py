class Editor:

    def __init__(self):
        self.__content = ""
        self.__states = [""]

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__states.append(self.__content)
        self.__content+=content


    def undo(self):
        if len(self.__states):
            self.__content = self.__states[-1]




