import random, string

amount = int(input('[Sub To Kosmo] Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Kosmo_Nitro.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[SUB2KOSMO]--[GENERATED] {code}')
    value += 1