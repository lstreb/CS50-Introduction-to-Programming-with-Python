def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

def main():
    sentence = input ("Type the sentence: ")
    sentence = convert(sentence)
    print(sentence)

main()