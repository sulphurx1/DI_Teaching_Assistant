from string import punctuation
from nltk.corpus import stopwords

class Text:
    def __init__(self, text):
        self.text = text

    def freq(self, word):
        return self.text.split(" ").count(word) if self.text.split(" ").count(word) > 0 else None
    
    
    
    
    
    def common(self):
        text_set = list(set(self.text.split(" ")))
        highest = text_set.pop(0)

        for word in text_set:
            if self.text.count(word) > self.text.count(highest):
                highest = word
        
        return highest
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def unique(self):
        return list(set(self.text.split(" ")))
    


    
    
    
    
    
    
    @classmethod
    def from_file(cls, text_file):
        with open(text_file) as f:
            word_list = f.readlines()
            word_list = [word.replace("\n", "") for word in word_list]
            return Text(" ".join(word_list))
        
















class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def de_punc(self):
        return "".join([word for word in self.text if punctuation.count(word) == 0])
    
    def de_stopwords(self):
        return "".join([word for word in self.text.split(" ") if stopwords.words('english').count(word) == 0])
    

book = Text.from_file("the_stranger.txt")
print(book.common())
print(book.unique())
print(book.freq("the"))
book2 = TextModification(book.text)
print(book2.de_punc())
print(book2.de_stopwords())

        