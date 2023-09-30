def is_spam_words(text:str, spam_words:list, space_around=False) -> bool:
    text = text.lower().replace('.', '')
    text_words = text.split()
    print(text_words)

    for spam_word in spam_words:
        if space_around:
            if spam_word.lower() in text_words:
                return True
            else:
                return False
        if spam_word.lower() in text:
            return True
        else:
            return False

print(is_spam_words('Молох бог ужасен.', ['лох'], True))
print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))