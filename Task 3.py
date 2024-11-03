user_input=input("Enter a String: ")
String=(user_input.replace('of','')).split()
acronym=""
for word in String:
    acronym=acronym+word[0].upper()
print(f'Acronym of {user_input} is {acronym}')
