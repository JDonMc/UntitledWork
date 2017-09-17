from PyDictionary import PyDictionary

dictionary = PyDictionary()
print(dictionary.meaning("indentation"))
print(dictionary.synonym("life"))
print(dictionary.antonym("paper"))
print(dictionary.translate("extreme", 'es'))

dictionary = PyDictionary("hotel","ambush","nonchalant","perceptive")
'There can be any number of words in the Instance'

print(dictionary.printMeanings()) # '''This print the meanings of all the words'''
print(dictionary.getMeanings()) # '''This will return meanings as dictionaries'''
print (dictionary.getSynonyms())

print (dictionary.translateTo("hi")) # '''This will translate all words to Hindi'''