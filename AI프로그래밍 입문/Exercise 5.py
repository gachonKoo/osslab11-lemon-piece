s = "t1 is the best team in the world"

vowels = "aeiouAEIOU"

result = s
for vowel in vowels:
    result = result.replace(vowel, "")

print(result)