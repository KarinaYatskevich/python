import string
class Alphabet:
    
    def __init__(self, land, letter):
        self.land = land
        self.letter = list(letter)
        
    def print(self):
        return self.letter
    
    def letters_num(self):
        len(self.letter)
    
    
class EngAlphabet(Alphabet):

    __letter_num = 26
    
    def __init__(self, ):
        super(EngAlphabet, self).__init__('En', string.ascii_uppercase)

    def __letters_num(self):
        return EngAlphabet.__letter_num

    def is_en_letter(self, let):
        if let.upper() in self.letter:
            return "yees"
        else:
            return 'nooo'

    @staticmethod
    def example():
        print("smth")

if __name__ == '__main__':
    e = EngAlphabet()
    print(e.print())
    print(e.letters_num())
    print(e.is_en_letter('F'))
    print(e.is_en_letter('Щ'))
    print(e.example())




    