#S in solid design principle
#Seperation of concern or Single Responsibility principle

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count+=1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    #Secondary responsibility added, which is a bad idea.
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):#functions are using lower alphabets with underscores
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


#Anti-pattern: God objects
#Single Responsibility prevents you from implementing it.


j = Journal()
j.add_entry("I exercised today.")
j.add_entry("I ate a bug")
print(f"Journal entries:\n{j}")
