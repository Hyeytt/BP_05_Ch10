import random                       # random 모듈을 사용하기위해 임포트함
from tkinter import                 # tkinter 라이브러리에서 모듈을 불러온다
window = Tk()                       # 윈도우 창을 생성한다 
secret_number = random.randint(1, 100) # 변수 secret.number에 1에서 100까지의 숫자중 랜덤한 수를 가져오는 속성을 부여한다
guess = None                        
num_guesses = 0                   # num_guesses의 변수값을 0으로 초기화시킨다

def guess_number():               # guess_number라는 함수를 정의내린다
  global num_guesses              # 전역변수 global을 사용하여 함수 뿐만이 아니라 스크립트 전제에서 이 변수를 사용할 수 있게 한다
  guess = int(entry.get())        # 입력하는 모든 숫자를 int함수를 사용해 정수로 변환시켜 변수 guess에 저장한다
  num_guesses += 1                # num_guessess는 숫자가 더해질 때마다 계속 더해진다 
  if guess == secret_number:      # 만약 입력한 guess 값이 랜덤한 수와 같다면
    message = "축하합니다!!"      # 축하합니다라는 메세지를 출력한다
  elif guess < secret_number:     # 만약 입력한 guess 값이 랜덤한 수보다 작다면
    message = "너무 낮아요!!"     # 너무 낮아요!! 라는 문장을 출력한다
  else:                           # 만약 입력한 guess 값이 랜덤한 수보다 크다면 
    message = "너무 높아요!!"     # 너무 높아요 라는 메세지가 출력되게 한다
  label['text']= message          # 입력된 값에 따른 메세지를 출력하는 라벨을 설정한다

def reset():                     # reset 함수를 정의내린다
  global num_guesses              # 전역변수 global을 사용하여 함수 뿐만이 아니라 스크립트 전제에서 이 변수를 사용할 수 있게 한다
  entry.delete(0, END)           # 숫자를 입력하는 칸 안의 숫자들을  초기화 한다 
  secret_number = random.randint(1, 100)  # 변수 secret.number에 1에서 100까지의 숫자중 랜덤한 수를 가져오는 속성을 부여한다
  guess = 0                     # guess의 값을 0으로 초기화 시킨다
  num_guesses = 0               # num_guesses의 변수값을 0으로 초기화시킨다
  message = "1부터 100사이의 숫자를 추측하시오"  # 변수 message에 "1부터 100사이의 숫자를 추측하시오"라는 문장을 저장한다
  label['text']= message         

message = "1부터 100사이의 숫자를 추측하시오"  
label = Label(window, text=message)         # "1부터 100사이의 숫자를 추측하시오"라는 문장을 윈도우 창의 라벨에 입력한다
entry = Entry(window)                       # enty(숫자를 입력하는) 창을 그 아래에 넣는다  

guess_button = Button(window, text="숫자를 입력", command=guess_number)  # "숫자를 입력" 이라는 문구를 누르면 숫자가 추가되는 버튼을 만든다
reset_button = Button(window, text="게임을 다시 실행", command=reset)    # "게임을 다시 실행이라는 문구를" 누르면 숫자가 초기화되는 버튼을 만든다

label.grid(row=0, column=0, columnspan=2, sticky=W+E)    # 처음 라벨의 크기를 정의내린다
entry.grid(row=1, column=0, columnspan=2, sticky=W+E)    # 숫자를 입력하는 entry 창의 크기를 정의내린다
guess_button.grid(row=2, column=0)                       # 숫자를 추가하는 버튼의 크기를 정의내린다
reset_button.grid(row=2, column=1)                      # 숫자를 초기화 시키는 버튼의 크기를 정의내린다
window.mainloop()                                      # 윈도우가 종료되기 전까지는 이 프로그램이 작동된다는 뜻의 문장이다
