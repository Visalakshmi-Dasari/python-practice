class Wordplay():
    def __init__(self,list_words):
        self.list_words=list_words

    def words_with_length(self , length):
        words_with_length=[]
        for word in self.list_words:
            if len(word)==length:
                words_with_length.append(word)
        return words_with_length
    def starts_with_s(self,s):
        starts_with_s=[]
        for word in self.list_words:
            if word[0]==s :
                starts_with_s.append(word)
        return starts_with_s

    def ends_with_s(self,s):
        ends_with_s=[]
        for word in self.list_words:
            if word[-1]==s :
                ends_with_s.append(word)
        return ends_with_s

    def palindromes(self):
        list_palindromes=[]
        for word in self.list_words:
            if word == word[::-1]:
                list_palindromes.append(word)
        return list_palindromes
s=Wordplay(['gdh','kid','kidd'])
print s.starts_with_s('k')
print s.words_with_length(4)
print s.palindromes()