from tkinter import *                                                # 반듯하게 나열하게 하는 fetch라는 함수를 표현사용한다.         
fields = '이름', '직업', '국적'
def fetch(entries):                                                  # field 에 해당하는 값을 입력하는 칸을초기화 시킨다
 for entry in entries:                                               # 입력한 값을 추가시킨다
     field = entry[0]
     text = entry[1].get()                                             
     print('%s: "%s"' % (field, text))                                               
def makeform(root, fields):                                            # makeform 함수를 정의내린다
     entries = []                                                      #  entry는 리스트의 내용을 다룬다
     for field in fields:                                              #  field 관련된 내용을 다룬다                                         
         row = Frame(root)
         lab = Label(row, width=15, text=field)                        # 관련 라벨의 크기를 정한다
         ent = Entry(row)                                              # 입력할 entry의 크기를 정한다 
         row.pack(side=TOP, fill=X)
         lab.pack(side=LEFT)
         ent.pack(side=RIGHT, expand=YES, fill=X)
         entries.append((field, ent))
     return entries
root = Tk()                                                            # 윈도우 창을 띄운다  
ents = makeform(root, fields)                                          # ents라는 변수에 설정해놓은 함수 makeform을 저장한다
root.bind('<Return>', (lambda event, e=ents: fetch(e)))                # #lambda라는 익명함수를 사용한다
b1 = Button(root, text='보여주기',                                     #
 command=(lambda e=ents: fetch(e)))
b1.pack(side=LEFT, padx=5, pady=5)                                  # pack()을 사용해 위치를 표현한다. b1은 왼쪽의 x: 5 y:5 에 위치시킨다
b2 = Button(root, text='종료하기', command=root.quit)               # b2는 누르면 나가지는 '종료하기' 표시가 있는 버튼이다
b2.pack(side=LEFT, padx=5, pady=5)                                  # pack()을 사용하여 위치를 표현한다. x: 5, y:5 엥 위치시킨다
root.mainloop()                                                      # root.mainloop()는 root 창은 종료되지 않고 사용자의 입력을 처리하는 등의 일을 계속 수행하게한다.
