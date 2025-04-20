# Get inputs
s1 = input()
s2 = input()

result = "" # store result

# Create an array to access letters by index
# z is essentially 0 as adding z to any letter will retain the same letter, and 26 % 26 = 0
letters = "zabcdefghijklmnopqrstuvwxy"
# Create a dictionary to access index by letter
alphabetIndices = { letters[i]:i for i in range(26) }

# For each index, add the pair of letters in those positions by adding their indices (mod 26) and then looking up their index in the letters array
for i in range(len(s1)):
    result += letters[(alphabetIndices[s1[i]] + alphabetIndices[s2[i]]) % 26]

# Output result
print(result)
