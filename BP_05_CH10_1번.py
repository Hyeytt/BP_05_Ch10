    from tkinter import Tk, Label, Button            # tkinter 라이브러리에서 모듈을 불러온다. tk(메인창), label(텍스트 또는 이미지), button(간단한 버튼)을 생성
    def greet():                                     # greet라는 함수를 정의내린다                                 
        print("파이썬에 오신 것을 환영합니다. ")     # greet이라는 함수에서는 print함수를 이용하여 "파이썬에 오신 것을 환영합니다. "를 출력한다

    window = Tk()                                    # 가장 상위레벨의 윈도우 창을 생성한다
    label = Label(window, text="간단한 GUI 프로그램!")  # 텍스트와 이미지를 나타내는 label 위젯을 사용하고 창 부분에 "간단한 GUI 프로그램!"라는 문구를 출력한
    label.pack()                                    #우선 자동정렬인 label.pack()을 사용하여 label을 위치시킨다 

    greet_button = Button(window, text="환영합니다.", command=greet) # 환영합니다 라는 문구를 출력하는 버튼을 greet_button이라는 변수에 저장한다. 버튼을 누를시 "파이썬에 오신 것을 환영합니다. "를 출력한다
    greet_button.pack()                             # pack()을 사용하여 greet_button의 위젯을 창에 위치시킨다

    close_button = Button(window, text="종료", command=window.quit) # 종료라는 문구를 출력하는 버튼을 close_button이라는 변수에 저장한다. 버튼을 누르면 창이 나가진다
    close_button.pack()                             # pack()을 사용하여 버튼을 위치시킨
    window.mainloop()                               # 이 윈도우 창을 윈도우가 종료될 때 까지 실행시킨다

