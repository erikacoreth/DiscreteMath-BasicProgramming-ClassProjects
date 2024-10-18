#Write a function encodeString that will encode a string like 'AAAAABBBBAAA' and return a list of tuples: [('A', 5), ('B', 4), ('A', 3)]
#meaning that the string has '5 a's, followed by 4 b's, followed by 3 a's.'.
#Wirte a corresponding function decodeString that will take in a list of tuples and print the original string.



def encodeString(stringVal):
    if not stringVal:
        return []
    encoded = []
    count = 1

    for i in range(1, len(stringVal)):
        if stringVal[i] == stringVal[i-1]:
            count += 1
        else:
            encoded.append((stringVal[i-1], count))
            count = 1

    encoded.append((stringVal[-1], count))

    return encoded

result = encodeString("AAAAABBBBAAA")
print(result)


def decodeString(encodedList):
    decoded = ''

    for char, count in encodedList:
        decoded += char * count

    return decoded

encoded_input = [('A', 5), ('B', 4), ('A', 3)]
result = decodeString(encoded_input)
print(result)

