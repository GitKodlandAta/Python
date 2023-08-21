import random
semboller = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
şifre = ''
uzunluk = int(input('Şifre uzunluğu kaç harf olsun? '))

for i in range(uzunluk):
    şifre += random.choice(semboller)

print(şifre)
