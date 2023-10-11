# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:53:55 2023

@author: OFA2KOR
"""
import random
letters=['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
num=['1','2','3','4','5','6','7','8','9','0']
symbols=['@','#','$','%','&','*','?']        
print("Welcome to PyPassword generator")
n_letters=int(input("How many letters you want in the password"))
n_symbols=int(input("How many symbols you want in the password"))
n_nums=int(input("How many numbers you want in the password"))
random_letters=random.sample(letters,n_letters)
random_symbols=random.sample(symbols,n_symbols)
random_nums=random.sample(num,n_nums)
password= random_letters+random_nums+random_symbols
pass_string = list(password)
random.shuffle(pass_string)
shuffled_string = ''.join(pass_string)
print("Your password is  :", shuffled_string)