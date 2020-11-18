# -*- coding: utf-8 _*_
import random
import os

def start_command(message):
     random.seed()
     with open(os.getcwd()+'\\data\\welcome.txt','r') as w:
         welcomes = [ c for c in w]
     i = random.randint(0,len(welcomes)-1)
     return welcomes[i]        