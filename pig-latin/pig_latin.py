VOWEL_SOUNDS = ['a', 'e', 'i', 'o', 'u'] #chokbar que 'y' ne soit pas dedans...
def translate(text):
    return ' '.join(map(translate_word, text.split()))
    

def translate_word(word):
    result = word
    first_letters = result[0]
    if first_letters in VOWEL_SOUNDS or result.startswith(('xr', 'yt')): #rule1
        result += 'ay'
    else:
        if result.startswith(('sch', 'thr')):
            first_letters = result[:3]
        elif result.startswith(('ch', 'st', 'rh', 'qu', 'th')):
            first_letters = result[:2]
        #rule 2
        result = result.replace(first_letters, '')
        to_add = 'ay' #by default only add ay at the end
        if result[:2] == 'qu': #rule 3
            result = result.replace('qu', '')
            to_add = 'quay'
        result = result + first_letters + to_add
    return result