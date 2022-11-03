# class Bankomat:
#     def __init__(self, parol):
#         self.parol = parol
#         if self.parol == 1111:
#             a = 100000
#             print(f"Balansda {a} so'm bor")
#         else:
#             print("Parol noto'g'ri")
    

#     def sms_qabul(self):
#         qwe = input("Sms qabul qiluvchi telefon raqamingini kiriting: +998")
#         if len(qwe) == 9:
#             print("Raqam muvaffaqiyatli qo'shildi")
#         else:
#             print("Raqam kiritishda xatolik")

#     def parolni_almashtir(self):
#         paroll = int(input("Eski parolni kiriting: "))
#         if paroll == self.parol:
#             son = int(input("Yangi parolni kiriting: "))
#             son1 = int(input("Yangi parolni yana bir bor kiriting: "))
#             if son == son1:
#                 print("Parol muvaffaqiyatli o'rnatildi")
#             else:
#                 print("Yangi parollar bir xil emas")
#         else:
#             print("Parol noto'gri") 
# s = Bankomat(parol = 1111)
# s.sms_qabul()






# class Manzil:
#     def __init__(self, viloyat, tuman, kocha, uy):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.kocha = kocha
#         self.uy = uy
#     def get_manzil(self):
#         return f"{self.viloyat.capitalize()}, {self.tuman.capitalize()}, {self.kocha.capitalize()}, {self.uy.capitalize()}"


# class Talaba:
#     def __init__(self, ism, familiya, t_yil, manzil):
#         self.ism = ism
#         self.familiya = familiya
#         self.t_yil = t_yil
#         self.manzil = manzil
#     def get_info(self):
#         return f"Ismi {self.ism.capitalize()}\nFamiliya {self.familiya.capitalize()}\nTug'ilgan yili {self.t_yil} yil\nManzil {self.manzil.get_manzil()}"

# man = Manzil("andijon", "paxtaobod", "oltin yo'l", "73")
# a = Talaba("maqsadbek", "ibrohimjonov", 2006,  man)
# print(a.get_info())



# class Odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
    
#     def tanishtir(self):
#         return f"{self.ism}, {self.yosh}"


# class Dasturchi(Odam):
#     def __init__(self, ism, yosh, tajriba):
#         super().__init__(ism, yosh)
#         self.tajriba = tajriba
#     def tanishtir1(self):
#         return f"{self.ism}, {self.yosh}, {self.tajriba}"

# b = Dasturchi('maqsadbek', 16, 'yaxshi') 
# print(b.tanishtir1())











# class Bankomat:
#      def __init__(self, parol):
#          self.parol = parol
#          self.k_parol = 1111
#          if self.parol == self.k_parol:
#              a = 100000
#              print(f"Balansda {a} so'm bor")
#              qwe = input("Pul yechishni istaysizmi: (ha/yoq) ")
#              if qwe == 'ha':
#                  qwer = int(input("Yechish kerak bo'lgan summani kiriting: "))
#                  if qwer > a:
#                      print("Balansda pul yetarli emas")
#                  else:
#                      a-=qwer
#                      print(f"Balansda {a} so'm qoldi")
                 
#              else:
#                  print("Xizmat ko'rsatish tugadi")
#          else:
#              print("Parol noto'g'ri")         
    
#      def sms_qabul(self):
#          tekshir = int(input("Telefon raqamni ulash uchun parolni kiriting: "))
#          if tekshir == self.k_parol:
#              qwe = input("Sms qabul qiluvchi telefon raqamingini kiriting: +998")
#              if len(qwe) == 9:
#                  print("Raqam muvaffaqiyatli qo'shildi")
#              else:
#                  print("Raqam kiritishda xatolik")
#          else:
#              print("Parolni xato kiritdiz")
     
     
     
#      def parolni_almashtir(self):
#          paroll = int(input("Eski parolni kiriting: "))
#          if paroll == self.k_parol:
#              son = int(input("Yangi parolni kiriting: "))
#              son1 = int(input("Yangi parolni yana bir bor kiriting: "))
#              if son == son1:
#                  print("Parol muvaffaqiyatli o'rnatildi")
#              else:
#                  print("Yangi parollar bir xil emas")
#          else:
#              print("Parol noto'gri") 
# s = Bankomat(parol =  1111)




# from uuid import uuid4
# a = uuid4()
# class Avto:
#     __soni = 0
#     def __init__(self, rang, nomi, narxi):
#         self.rang = rang
#         self.nomi = nomi
#         self.narxi = narxi
#         self.km = 0
#         self.id = uuid4()
#         Avto.__soni+=1
#     def change_id(self, qiymat):
#         self.__id = qiymat
#     def add_probeg(self, qosh):
#         self.qosh = qosh
#         self.km+=qosh
#     def get_id(self):
#         print(f"{self.__id}")
#     def qwe(self):
#         print(f"Rangi: {self.rang}, Nomi: {self.nomi}, Narxi: {self.narxi}, Probeg: {self.km}")
#     def soni(cls):
#         print(cls.__soni)
# m1 = Avto("Sariq", 'Spark', '2500$')
# m1.soni()
# m1.qwe()



# class Talaba:
#     def __init__(self, ism, familiyasi):
#         self.ism = ism
#         self.familiyasi = familiyasi
#     def tanishtir(self):
#         return f"Ism :{self.ism}, {self.familiyasi}"


# class Tajriba:
#     def __init__(self, ism, familiyasi, t_yil):
#         super().__init__(ism, familiyasi)
#         self.t_yil = t_yil
#     def tanishtir1(self):
#         print(f"Ism: {self.ism}, Familiyasi: {self.ism}, Tugilgan yili: {self.t_yil}")

# ad = Tajriba('ag', 'jhgd', 2006)

# ad.tanishtir1()


# son = int(input())
# for _ in range(10):
#     son*=2
#     print(son)


# raqamlar = [55, 44, 33, 22]
# print(max(min(raqamlar[:2]), abs(-42)))

# raqamlar = [1, 2, 3, 4, 5, 6]
# raqamlar2 = [0, 1, 2, 3]
# raqamlar += raqamlar2
# raqamlar.reverse()
# print(raqamlar[-4])

# from random import*




# a = 0
# for i in range(0, 131):
#     if i%7==0:
#         a+=i   
# print(a)


# a = 0
# for i in range(7, 131, 7):
#     a+=i
# print(a)



# q = ['ona', 'mat', 'ing', 'rus', 'fiz']

# from random import *
# oquvchi = {}
# for i in range(5):
#     nom = input(f'{i+1} - Ism: ').capitalize()
#     a = choice(q)
#     oquvchi[nom] = {a:randint(0, 5),
#     a:randint(0, 5),
#     a:randint(0, 5),
#     a:randint(0, 5),
#     a:randint(0, 5)}
#     q.remove(a)
# print(oquvchi)

# import random
# sn = {}
# q = ['ona', 'mat', 'ing', 'rus', 'fiz']
# ismlar = ['Maqsadbek', 'Xalilillo', 'Nurmuhammad', 'Bobur']
# random.shuffle(ismlar)
# for i in ismlar:
#     sn[i] = {}
# for i in ismlar:
#     random.shuffle(q)
#     for f in q:
#         sn[i][f] = random.randint(3, 5)
# print(sn)

# n = int(input('Son kiriting: '))
# for i in range(n):
#     for j in range(n-i-1):
#         print('', end = ' ',)
#     for j in range(i+1):
#         print('*', end = ' ')
#     print()