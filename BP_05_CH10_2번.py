from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E     # tkinter 라이브러리에서 tk, label, button, entry(한 줄로된 단순한 박스 ),
                                                                    # IntVar(정수 자료형을 선언하는 위젯), END(맨 끝의 위치에 텍스트 문을 입력한다는 뜻), W,e (라벨안에서의 위치)

def update_add():                                                   # undate_add라는 함수를 정의내린다
    update("add")                                                   # update 함수를 사용하여 "add"의 속성을 추가한다
def update_subtract():                                              # update_subtract라는 함수를 정의내린다
    update("subtract")                                              # update 함수를 사용하여 subtract의 속성을 추가한다
def update_reset():                                                 # update_reset이라는 함수를 정의내린다   
    update("reset")                                                 # update 함수를 사용하여 reset 의 속성을 추가한다

window = Tk()                                                       # 가장 상위레벨의 윈도우 창을 생성한다
total = 0                                                           # 오류 방지를 위해 먼저 total 값을 0으로 초기화 시킨다
sum = Label(window)                                                # sum이라는 변수에 윈도우의 창 모양 라벨 속성을 부여한다 
sum.grid(row=0, column=1, columnspan=2)                             # 그리드의 위치를 설정하는 문장이다. grid 안의 행과 열값을 각각 0과 1로 설정한다, 폭의 넚이는 2로 한다

label = Label(window, text="현재 합계:")                           # 윈도우 창의 라벨에는 "현재 합계"라는 텍스트를 출력한다
label.grid(row=0, column=0)                                        # grid의 행과 열의 위치는 각각 0,0이다

entry = Entry(window)                                             #
entry.grid(row=1, column=0, columnspan=3)

add_button = Button(window, text="더하기(+)", command=update_add)
subtract_button = Button(window, text="빼기(-)", command=update_subtract)
reset_button = Button(window, text="초기화", command=update_reset)

add_button.grid(row=2, column=0)
subtract_button.grid(row=2, column=1)
reset_button.grid(row=2, column=2)

def update(method):
  global total
  if method == "add":
    total += int(entry.get())
  elif method == "subtract":
    total -= int(entry.get())
  else:
    total = 0
  sum['text'] = str(total)
  entry.delete(0, END)
window.mainloop()
