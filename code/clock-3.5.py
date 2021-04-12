#coding=utf-8
# import network
# import ntptime

# from machine import Pin, SPI

import os
# import framebuf
import time
import random
import sys

print("Hello python")

def display_digit(display_num, digit):
    """
    @display: int display index
    @digit: int from 0 to 9 inclusive

    Given an integer digit, fetches a random MNIST image,
    upscales it and displays it on the eink display
    """
    digit = digit % 10
    digit_data = read_digit_data(digit)
    
    for i in range(196):
        if (i>0 and i%7 == 0):
            print("", flush=True)
        # 196 bytes for each digit (28 pixels)*(28 pixels)*(2 bits/pixel)/8
        for j in range(4):
        # 4 pixels of data stored in in each byte at 2 bits/pixel
            pixel_num = i * 4 + j
            pixel_i = pixel_num // 28   # pixel i in mnist data
            pixel_j = pixel_num % 28    # pixel j in mnist data
            
            pixel_value = (digit_data[i] >> (2*j)) & 0b11 # 2bpp grey value
            
            if (pixel_value == 0):
                print(pixel_value, sep='', end=' ', file=sys.stdout, flush=True)
            if (pixel_value == 1):
                print("\033[31m"+ str(pixel_value) + "\033[0m", sep='', end=' ', file=sys.stdout, flush=True)
            if (pixel_value == 2):
                print("\033[32m"+ str(pixel_value) + "\033[0m", sep='', end=' ', file=sys.stdout, flush=True)
            if (pixel_value == 3):
                print("\033[34m"+ str(pixel_value) + "\033[0m", sep='', end=' ', file=sys.stdout, flush=True)

def display_digit_opt1(display_num, digit_0, digit_1, digit_2, digit_3, digit_4, digit_5):
    
    digit_data_0 = read_digit_data(digit_0)
    digit_data_1 = read_digit_data(digit_1)
    digit_data_2 = read_digit_data(digit_2)
    digit_data_3 = read_digit_data(digit_3)
    digit_data_4 = read_digit_data(digit_4)
    digit_data_5 = read_digit_data(digit_5)
    
    for i in range(196):
        
        # 196 bytes for each digit (28 pixels)*(28 pixels)*(2 bits/pixel)/8
        for j in range(4):
            
            pixel_value = (digit_data_0[i] >> (2*j)) & 0b11 # 2bpp grey value
            
            if (pixel_value == 0):
                print(pixel_value, sep='', end='', file=sys.stdout, flush=False)
            if (pixel_value == 1):
                print("\033[31m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
            if (pixel_value == 2):
                print("\033[32m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
            if (pixel_value == 3):
                print("\033[34m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
        
        if (i>0 and (i+1)%7 == 0):
            for m in range(i-7, i):
                for n in range(4):
                    pixel_value = (digit_data_1[m] >> (2*j)) & 0b11 # 2bpp grey value
                    
                    if (pixel_value == 0):
                        print(pixel_value, sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 1):
                        print("\033[31m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 2):
                        print("\033[32m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 3):
                        print("\033[35m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
            
        if (i>0 and (i+1)%7 == 0):
            print(' ', sep='', end=' ', file=sys.stdout, flush=False)
            for m in range(i-7, i):
                for n in range(4):
                    pixel_value = (digit_data_2[m] >> (2*j)) & 0b11 # 2bpp grey value
                    
                    if (pixel_value == 0):
                        print(pixel_value, sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 1):
                        print("\033[31m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 2):
                        print("\033[32m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 3):
                        print("\033[35m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
            
        if (i>0 and (i+1)%7 == 0):
            for m in range(i-7, i):
                for n in range(4):
                    pixel_value = (digit_data_3[m] >> (2*j)) & 0b11 # 2bpp grey value
                    
                    if (pixel_value == 0):
                        print(pixel_value, sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 1):
                        print("\033[31m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 2):
                        print("\033[32m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 3):
                        print("\033[35m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
        
        if (i>0 and (i+1)%7 == 0):
            print(' ', sep='', end=' ', file=sys.stdout, flush=False)
            for m in range(i-7, i):
                for n in range(4):
                    pixel_value = (digit_data_4[m] >> (2*j)) & 0b11 # 2bpp grey value
                    
                    if (pixel_value == 0):
                        print(pixel_value, sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 1):
                        print("\033[31m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 2):
                        print("\033[32m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 3):
                        print("\033[35m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
            
        if (i>0 and (i+1)%7 == 0):
            for m in range(i-7, i):
                for n in range(4):
                    pixel_value = (digit_data_5[m] >> (2*j)) & 0b11 # 2bpp grey value
                    
                    if (pixel_value == 0):
                        print(pixel_value, sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 1):
                        print("\033[31m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 2):
                        print("\033[32m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
                    if (pixel_value == 3):
                        print("\033[35m"+ str(pixel_value) + "\033[0m", sep='', end='', file=sys.stdout, flush=False)
            print("", flush=True)

def display_digit_opt2(digit_0, digit_1, digit_2, digit_3):

    global g_digit_data_0, g_digit_data_1, g_digit_data_2, g_digit_data_3
    
    if (digit_0 != -1):
        g_digit_data_0 = convert_digit_data(digit_0)
    if (digit_1 != -1):
        g_digit_data_1 = convert_digit_data(digit_1)
    if (digit_2 != -1):
        g_digit_data_2 = convert_digit_data(digit_2)
    if (digit_3 != -1):
        g_digit_data_3 = convert_digit_data(digit_3)
    
    data = ''
    # row
    for i in range(28):
        # digit position
        for j in range(4):
            # column
            for k in range(28):
                if j%4 == 0:
                    data += str(g_digit_data_0[i*28 + k])
                if j%4 == 1:
                    data += str(g_digit_data_1[i*28 + k])
                if j%4 == 2:
                    data += str(g_digit_data_2[i*28 + k])
                if j%4 == 3:
                    data += str(g_digit_data_3[i*28 + k])
            if j==1:
                data += ' '
        data += '\n'
    return data

def convert_digit_data(digit):
    digit_data = read_digit_data(digit)
    data = []
    for i in range(196):
        # 196 bytes for each digit (28 pixels)*(28 pixels)*(2 bits/pixel)/8
        for j in range(4):
            pixel_value = (digit_data[i] >> (2*j)) & 0b11 # 2bpp grey value
            data.append(pixel_value)
    return data

def read_digit_data(digit):
    """
    @digit: int from 0 to 9 inclusive

    Given a digit, fetches a random MNIST digit and returns the raw
    binary data for its image at greyscale depth of 2 bits per pixel.
    Returns a bytearray of length (28*28)*2/8 = 196 in little endian
    """
    fn = 'digit_%d.data' % digit # filename where images for digit are stored
    fsize = os.stat(fn)[6]       # filesize
    N = fsize // 196             # number of images in file
    n = random.randint(0, N - 1) # pick a random index

    # fetch image
    f = open(fn, 'rb')
    f.seek(n*196)
    data = f.read(196)
    f.close()

    return data

def main():

    last_digit_0 = -1
    last_digit_1 = -1
    last_digit_2 = -1
    last_digit_3 = -1

    while True:
        
        the_time = time.localtime()
        digit_0 = the_time[4] // 10
        digit_1 = the_time[4] % 10
        digit_2 = the_time[5] // 10
        digit_3 = the_time[5] % 10
        #digit_4 = the_time[5] // 10
        #digit_5 = the_time[5] % 10
        # print(digit_0, digit_1, flush = True)
        # display_digit_opt1(0, digit_0, digit_1, digit_2, digit_3, digit_4, digit_5)
        
        
        print(display_digit_opt2(
            -1 if digit_0 == last_digit_0 else digit_0, 
            -1 if digit_1 == last_digit_1 else digit_1, 
            -1 if digit_2 == last_digit_2 else digit_2, 
            -1 if digit_3 == last_digit_3 else digit_3 ), flush=True)

        last_digit_0 = digit_0
        last_digit_1 = digit_1
        last_digit_2 = digit_2
        last_digit_3 = digit_3
        
        time.sleep(1)

main()