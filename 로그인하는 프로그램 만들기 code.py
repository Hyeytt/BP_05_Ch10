from tkinter import Tk, Label, Entry ,Button                # tkinter 라이브러리에서 모듈을 불러온다
window = Tk()                        # 윈도우 창을 띄운다 
label1 = Label(window, text="로그인 하세요!!!", font=("Helvetica", 20)) #변수 라벨1에 "로그인 하세요!!!"라는 문장을 "Helvetica"라는 폰트로 20의 크기만큼 적는 문장을 저장한다
label1.pack()                                                          # pack()을 활용하여 위치를 설정한다. 
label2 = Label(window, text="아이디")                                  # "아이디"라는  문장을 출력하는 라벨을 label1에 저장한다 
label2.pack()                                                          # label2를 pack()을 활용해 label1의 아래에 위치시킨다
entry1 = Entry(window)                                                 # 아이디를 입력받게 하는 공간을 entry를 통해 표현한다
entry1.pack()                                                         # pack()을 활용해 entry1을 출력한 단어인  '아이디' 아래에 위치시킨다
label2 = Label(window, text="패스워드")                               # "패스워드"라는 단어를  출력하는 라벨을 label2에 저장한다
label2.pack()                                                        # pack()을 활용해 entry1 아래에 위치시킨다
entry2 = Entry(window)                                                #  entry2는 패스워드를 입력할 공간이다
entry2.pack()                                                        # pack()을 활용해  아래에 위치시킨다
button1 = Button(window, text="로그인")                               # 로그인이라고 써있는 버튼을 생성한다    
button1.pack()                                                      # 맨 아래에 버튼을 위치시킨
window.mainloop()
