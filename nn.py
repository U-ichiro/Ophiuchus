# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      U16
#
# Created:     02/05/2017
# Copyright:   (c) U16 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def odd_or_even():
    for i in range(1,6):
        if i % 2 != 0:
            print("{0} is odd".format(i))
        else:
            print("{0} is even".format(i))


if __name__ == "__main__":
    odd_or_even()
    print("こんにちは世界")