#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    p = input('Введите предложение: ')
    tmp = p.split()
    f = False
    for i in tmp:
        if len(i) > 10:
            f = True
            break
    if f:
        print('Самое длинное слово имеет больше 10 символов')
    else:
        print('Самое длинное слово НЕ имеет больше 10 символов')
