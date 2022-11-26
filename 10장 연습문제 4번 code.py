from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E,StringVar  # tkinter 라이브러리에서 모듈을 불러온다
def do_convert():                                    # co_convert 함수를 설정하여 어떻게 인치를 센티미터로 변환할지에 대한 방법을 정의내린다
    inch_val = float(cvt_from.get())                 # inch_val이라는 변수에 입력받은 수를 float함수를 사용해 실수로 변환시켜 저장한다 
    centimeters_val = inch_val * 2.54                # 인치를 센티미터로 변환하는데 그 방법을 설명하는 문장이다 
    cvt_to.set('%s 센티미터' % centimeters_val)      
    
root = Tk()                                            # 윈도우 창을 띄운다
cvt_from = StringVar()                                   
cvt_to = StringVar()

lbl = Label(root, text='인치를 센티미디로 변환하는 프로그램:') # '인치를 센티미디로 변환하는 프로그램'을 윈도우 라벨에 출력하는 문장을 변수 lbl에 저장한다
lbl.grid(row=0, column=0, columnspan=2)                        # lbl의 크기를 정하는 문장이다
from_lbl = Label(root, text='인치를 입력하시오:')              # '인치를 입력하시오:'라는 문장을 출력하는 라벨을 설정한다
from_lbl.grid(row=1, column=0)                                 # 그리고 그 크기를 설정하는 문장이다 
from_entry = Entry(root, textvariable=cvt_from)               # 인치값을 입력 받을 공간(entry)을 설정하는 문장이다
from_entry.grid(row=1, column=1)                              # 그 한줄로된 문장의 크기를 설정하는 문장이다 

to_lbl = Label(root, text='변환결과:')                        # 변환된 결과값 옆에 '변환결과' 라는 문장을 출력하는 라벨을 설정하는  문장이다 를 
to_lbl.grid(row=2, column=0)                                 #  그 크기를 정하는 문장이다
result_lbl = Label(root,textvariable=cvt_to)                  # 최종적으로 변환된 센티미터가 출력되는 라벨을 설정하는 문장이다
result_lbl.grid(row=2, column=1)                             # 그리고 그 크기를 정하는 문장이다 

convert_btn = Button(root,text='변환!', command=do_convert)  # '변환'이라는 버튼을 눌렀을때 프로그램이 작동되도록 하는 버튼을 설정하는 문장이다
convert_btn.grid(row=3, column=1)                            # 그리고 그 버튼의 크기를 정하는 문장이다 
root.mainloop()                                           
