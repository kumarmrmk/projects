from translate import Translator
translator=Translator(to_lang=input("enter lang u want: "))
translation = translator.translate(input("enter sentence to translate: "))
print(translation)
