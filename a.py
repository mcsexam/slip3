punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")
no_punct = ""
for char in my_str:
if char not in punctuations:
no_punct += char
print("String without punctuation:", no_punct)
