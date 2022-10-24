#def without_vowels(words):
    #vowels = 'aeiou'
    #print(''.join([I for I in words if I not in vowels]))


#if __name__ == '__main__':
    #n = input()
    #without_vowels(n)

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [ch for ch in text if ch.lower() not in vowels]
print(''.join(result))