from tkinter import *


tk = Tk()

label = Label(tk,text="Hello World!")

label.pack()

tk.mainloop()
'''
import tkinter.ttk as ttk
from tabulate import tabulate

tabulate.WIDE_CHARS_MODE = False

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 199)

root = Tk()
root.title("동물병원,동물약국 찾기")
root.geometry("1000x600")

csv1 = pd.read_csv('C:\\Users\\CHOI JUN HYUK\\Downloads\\전라북도 전주시_동물약국현황_20210722.csv',names=['사업장명', '도로명주소','지번주소', '소재지전화번호', '데이터기준일자', '위도', '경도', '동'],encoding='CP949')
csv2 = pd.read_csv('C:\\Users\\CHOI JUN HYUK\\Downloads\\전라북도 전주시_동물병원 현황_20210722.csv',names=['사업장명', '도로명주소','지번주소', '전화번호', '데이터기준일자', '동', '위도', '경도'],encoding='CP949')

label_n = Label(root, text="알아보고싶은 약국이름을 입력하세요")
label_n.pack()
label_n.place(x=10, y=50)

label_n2 = Label(root, text="거주하고 있는 동을 골라주세요")
label_n2.pack()
label_n2.place(x=10, y=100)

label_n3 = Label(root, text="알아보고싶은 병원이름을 입력하세요")
label_n3.pack()
label_n3.place(x=250, y=50)
'''
print("hello world")
