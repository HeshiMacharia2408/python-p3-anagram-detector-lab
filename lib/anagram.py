class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        
        for word in word_list:
            if word.lower() != self.word and sorted(word.lower()) == sorted_word:
                matches.append(word)
                
        return matches
    
listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
