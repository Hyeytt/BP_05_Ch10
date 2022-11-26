from random import *
from tkinter import *
          # 선택 하는 부분
def user_choice_rock():                           #  user_choice_rock()함수를 설정한다
  user_choice = "rock"                            #  유저의 선택이 바위인 경우
  turn(user_choice)                               
  user_image.configure(image=rock_image)          # 바위 사진을 올린다
def user_choice_paper():                          #  user_choice_paper()함수를 설정한다
  user_choice = "paper"                           #  유저의 선택이 보인 경우
  turn(user_choice)                            
  user_image.configure(image=paper_image)         #  보자기 사진을 올린다
def user_choice_scissors():                       # user_choice_scissors()함수를 설정한다
  user_choice = "scissors"                        # 유저의 선택이 가위인 경우
  turn(user_choice)                          
  user_image.configure(image=scissors_image)      # 가위사진을 올린다  

# 게임부분
def turn(user_choice):                            # turn(user_choice)함수를 설정한다
  oppo = ['rock', 'paper', 'scissors']            # 가위 바위 보 세가지 선택지가 있다.
  oppo_choice=oppo[randint(0,2)]                  # 3가지중 랜덤하게 선택한다 
  if(oppo_choice=='rock'):                        # 랜덤한 선택이 바위라면 
      oppo_image.configure(image=rock_image)      # 바위 사진을 올려 놓는다
      if(user_choice=='paper'):                   # 유저의 선택이 보라면
          turn_result.configure(text="사용자 승!", fg="green") # 사용자 승이라는 문장을 초록색으로 출력한다
          compare.configure(text=">>>>>")         # 비교문인 >>>>>를 출력한다
      elif(user_choice=='scissors'):              # 만약 유저의 선택이 가위라면 
          turn_result.configure(text="컴퓨터 승!", fg="red")   # 켬퓨터 승!이라는 문장을 빨간색으로 출력한다
          compare.configure(text="<<<<<")         # 비교문인 <<<<<<<<<<를 출력한다 
      else:
          turn_result.configure(text="무승부", fg="gray")  # 그 외의 경우에는 회색으로 무승부라는 문장을 출력한다 
          compare.configure(text="=====")         # ======라는 비교표현을 사용한다

  elif(oppo_choice=='paper'):                     # 랜덤한 선택이 보라면  
      oppo_image.configure(image=paper_image)     # 보 사진을 올려 놓는다
      if(user_choice=='scissors'):                # 만약 유저의 선택이 가위라면
          turn_result.configure(text="사용자 승!", fg="green") # 사용자 승이라는 문장을 초록색으로 출력한다
          compare.configure(text=">>>>>")         # 비교문인 >>>>>를 출력한다
      elif(user_choice=='rock'):                  # 만약 유저의 선택이 바위라면
          turn_result.configure(text="컴퓨터 승!", fg="red")  # 컴퓨터 승!이라는 문장을 빨간색으로 출력한다
          compare.configure(text="<<<<<")                     # 비교문인 <<<<<<<<<<를 출력한다
      else:                                                 # 그 외의 경우에는 
          turn_result.configure(text="무승부", fg="gray")   # 회색으로 무승부라는 문장을 출력한다 
          compare.configure(text="=====")                    # ======라는 동치표현을 사용한다
             
  elif(oppo_choice=='scissors'):                            # 랜덤한 선택이 가위라면     
            oppo_image.configure(image=scissors_image)  # 가위사진을 올려 놓는다
            if(user_choice=='rock'):                    # 만약 선택이 바위라면
                  turn_result.configure(text="사용자 승!", fg="green")          # 사용자 승이라는 문장을 초록색으로 출력한다
                  compare.configure(text=">>>>>")                               # 비교문인 >>>>>를 출력한다                                      
            elif(user_choice=='paper'):                                         # 만약 유저의 선택이 보자기라면
                  turn_result.configure(text="컴퓨터 승!", fg="red")            # 컴퓨터 승!이라는 문장을 빨간색으로 출력한다
                  compare.configure(text="<<<<<")                               # 동시에 비교문인 <<<<<<<<<<를 출력한다  
            else:
                  turn_result.configure(text="무승부", fg="gray")             # 그 외의 경우에는 회색으로 무승부라는 문장을 출력한다 
                  compare.configure(text="=====")                             # ======라는 동치표현을 사용한다     



  # 메인 프로그램                   
main_window = Tk()                                                              # 초기 윈도우 창을 띄운다
rock_button = Button(main_window, width=20, text="바위", justify=CENTER,       # 바위라고 써있는  버튼을 맨 왼쪽에 20의너비로  설정하는 문장이다  
command=user_choice_rock, activebackground='black', activeforeground='white')  #  누를때 배경이  검은색으로 표시되게 한다 글자는 하얀색으로 표시되게한다
paper_button = Button(main_window, width=20, text="보", justify=CENTER,        # 보라고 써있는  버튼을 가운데에 20의너비로  설정하는 문장이다  
command=user_choice_paper, activebackground='black', activeforeground='white') #  누를때 배경이  검은색으로 표시되게 한다 글자는 하얀색으로 표시되게한다
scissors_button = Button(main_window, width=20, text="가위", justify=CENTER,   # 가위라고 써있는  버튼을 가운데에 20의너비로  설정하는 문장이다  
command=user_choice_scissors, activebackground='black', activeforeground='white')    #  누를때 배경이  검은색으로 표시되게 한다 글자는 하얀색으로 표시되게한다
rock_image = PhotoImage(file="c:/rock.gif")                              # 바위 사진을 미리 저장하여 그 위치를 밝힌다 
paper_image = PhotoImage(file="c:/bo.gif")                               # 보자기 사진을 미리 저장하여 그 위치를 밝힌다 
scissors_image = PhotoImage(file="c:/gawi.gif")                           # 가위 사진을 미리 저장하여 그 위치를 밝힌다  
user_image = Label(text="사용자", image=rock_image)                       # 사용자 라는 텍스트가 쓰여있는 라벨을적는다
user_image.image = rock_image                                             # 유저의 이미지에는 바위그림을 올려놓는다 
compare = Label(main_window, justify=CENTER, font=("Helvetica", 30))      #
oppo_image = Label(text="컴퓨터",image=paper_image)                      # 반대의 그림에는 보자기 그림을 그려놓는다
oppo_image.image = paper_image                                           # 반대에는 보자기그림을 그려놓는다 
turn_result = Label(main_window, width=20, justify=CENTER, font=("Helvetica", 20))

  # 그리드 생성
rock_button.grid(row=5, column=1)                        # 바위 버튼 모양을 규정하는 문장이다
paper_button.grid(row=5, column=2)                      # 보자기 버튼 모양을 규정하는 문장이다  
scissors_button.grid(row=5, column=3)                    # 가위 버튼 모양을 규정하는 문장이다
user_image.grid(row=3, column=1)                         
compare.grid(row=3, column=2)                            
oppo_image.grid(row=3, column=3)                              
turn_result.grid(row=4, column=2)                       
  # GUI화면 루프처리
main_window.mainloop()                                  # 종료버튼을 누를때까지 프로그램은 작동된다
