string = "pojeiuazx"
def check(strings):
  vowels ="aeiou"
  s = set()
  for char in strings:
    if char in vowels:
      s.add(char)
    

  if len(vowels) == len(s):
    print("Accepted")
  else:
    print("Not Accepted")

check(string)
vowels =set("aeiou")
