def rev(string):
    return string[::-1]

def palin(string):
    if string == string[::-1]:
        return f'Yes, "{string}" is a palindrome.'
    else:
        return f'No, "{string}" is not a palindrome.'

def vowles(char):
    if char.lower() in 'aeiou':
        return f'Yes, "{char}" is a vowel.'
    else:
        return f'No, "{char}" is not a vowel.'

if __name__ == '__main__':
    print(rev("example"))
    print(palin("racecar"))
    print(vowles("a"))
