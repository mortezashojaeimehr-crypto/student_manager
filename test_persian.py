import sys
import io
import arabic_reshaper

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def farsi_print(text):
    reshaped = arabic_reshaper.reshape(text)
    print(reshaped)

farsi_print("کیرم تو برنامه نویسی")

