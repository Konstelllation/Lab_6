#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    p = input("Введите предложение: ")
    sl_2 = input("Введите букосочетание из двух букв: ")
    sl_n = input("Введите букосочетание: ")

    print('Количество буквосочетания ро в предложении = ', p.count('po'))
    print('Количество буквосочетания ', sl_2, ' в предложении = ', p.count(sl_2))
    print('Количество буквосочетания ', sl_n, ' в предложении = ', p.count(sl_n))
