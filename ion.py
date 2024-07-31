question_index=True
flipper=True
nota=0
grey=(128,128,128)
import time
import pygame
pygame.init()
from pygame import mixer
mixer.init()
music_path=r"C:\\Users\\user\\Desktop\\Autumn-Scene(chosic.com).mp3"
mixer.music.load(music_path)
mixer.music.play(-1)
liviu0=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\liviu.jpg")
liviu1=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\liviu1.jpg")
dirt_kiss=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\dirt_kiss.jpg")
violence=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\violence.jpg")
ion1=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\ion1.jpg")
icon=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\icon.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Test Ion")
font2=pygame.font.Font("freesansbold.ttf",15)
def end_background():
    window.blit(ion1,[0,0])
def background_corect():
    window.blit(liviu0, [0, 0])
    window.blit(liviu0, [wwidth // 2, 0])
def background_corect1():
    window.blit(dirt_kiss, [0, 0])
def background_gresit():
    window.blit(liviu1, [0, 0])
def background_gresit1():
    window.blit(violence,[0,0])
background_color=(140,180,0)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
wheight=600;
wwidth=1000;
window=pygame.display.set_mode((wwidth,wheight))
window.fill(background_color)
running=True
#start_question 1
question1='1.Este "Ion" de Liviu Rebreanu un roman :'
font1=pygame.font.Font("freesansbold.ttf",32)
text0='Test cu 10 intrebari si raspunsuri : "Ion" de Liviu Rebreanu'
text0=font1.render(text0,True,black,background_color)
text_rect0=text0.get_rect()
text_rect0.center=(wwidth//2,wheight//2)
window.blit(text0,text_rect0)
pygame.display.flip()
pause=True
for i in range(5):
    if pause==True:
        time.sleep(1)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            pause=False

window.fill(background_color)
text1=font1.render(question1,True,black,background_color)
text_rect1=text1.get_rect()
text_rect1.center=(wwidth//2,140)
A1="A.Subiectiv"
B1="B.Obiectiv"
#variantaA1
textA1=font1.render(A1,True,blue,green)
text_rectA1=textA1.get_rect()
text_rectA1.center=(wwidth//2-200,wheight//2+50)
#variantaB1
textB1=font1.render(B1,True,blue,green)
text_rectB1=textB1.get_rect()
text_rectB1.center=(wwidth//2+200,wheight//2+50)
corect1="Corect.Ion este un roman obiectiv."
gresit1="Gresit.Ion este un roman obiectiv."
#end_question_1



#start_question 2
question2='2.Ion apartine curentului literar :'
text2=font1.render(question2,True,black,background_color)
text_rect2=text1.get_rect()
text_rect2.center=(wwidth//2,140)
A2="A.Modernism"
B2="B.Realism"
C2="C.Romantism"
#variantaA2
textA2=font1.render(A2,True,blue,green)
text_rectA2=textA2.get_rect()
text_rectA2.center=(wwidth//2-300,wheight//2+50)
#variantaB2
textB2=font1.render(B2,True,blue,green)
text_rectB2=textB2.get_rect()
text_rectB2.center=(wwidth//2,wheight//2+50)
#variantaC2
textC2=font1.render(C2,True,blue,green)
text_rectC2=textC2.get_rect()
text_rectC2.center=(wwidth//2+300,wheight//2+50)
corect2="Corect.Ion apartine curentului literar realist."
gresit2="Gresit.Ion apartine curentului literar realist."
#end_question_2


#start_question 3
question3='3.Perspectiva narativa este :'
text3=font1.render(question3,True,black,background_color)
text_rect3=text3.get_rect()
text_rect3.center=(wwidth//2,140)
A3="A.La persoana 3,dindarat"
B3="B.La persoana 1 ,dindarat"
C3="C.La persoana 2 ,din spate"
#variantaA3
textA3=font1.render(A3,True,blue,green)
text_rectA3=textA3.get_rect()
text_rectA3.center=(wwidth//2-250,wheight//2+50)
#variantaB3
textB3=font1.render(B3,True,blue,green)
text_rectB3=textB2.get_rect()
text_rectB3.center=(wwidth//2+100,wheight//2+50)
#variantaC3
textC3=font1.render(C3,True,blue,green)
text_rectC3=textC2.get_rect()
text_rectC3.center=(wwidth//2,wheight//2+150)
corect3="Corect.perspectiva narativa este la pers. 3 dindarat."
gresit3="Gresit.Perspectiva narativa este la pers. 3 dindarat."
#end_question_3



#start_question 4
question4='4.Perioada literara in care Ion se incadreaza este :'
text4=font1.render(question4,True,black,background_color)
text_rect4=text4.get_rect()
text_rect4.center=(wwidth//2,140)
A4="A.postbelica"
B4="B.precambriana"
C4="C.interbelica"
#variantaA4
textA4=font1.render(A4,True,blue,green)
text_rectA4=textA4.get_rect()
text_rectA4.center=(wwidth//2-300,wheight//2+50)
#variantaB4
textB4=font1.render(B4,True,blue,green)
text_rectB4=textB4.get_rect()
text_rectB4.center=(wwidth//2,wheight//2+50)
#variantaC4
textC4=font1.render(C4,True,blue,green)
text_rectC4=textC4.get_rect()
text_rectC4.center=(wwidth//2+300,wheight//2+50)
corect4="Corect.Perioada este interbelica"
gresit4="Gresit.Perioada este interbelica."
#end_question_4



#start_question 5
question5='5.Personajul care la ucis pe Ion se numeste :'
text5=font1.render(question5,True,black,background_color)
text_rect5=text5.get_rect()
text_rect5.center=(wwidth//2,140)
A5="A.Razvan"
B5="B.Marcel"
C5="C.George"
D5="D.Ana"
#variantaA5
textA5=font1.render(A5,True,blue,green)
text_rectA5=textA5.get_rect()
text_rectA5.center=(wwidth//2-300,wheight//2+50)
#variantaB5
textB5=font1.render(B5,True,blue,green)
text_rectB5=textB5.get_rect()
text_rectB5.center=(wwidth//2,wheight//2+50)
#variantaC5
textC5=font1.render(C5,True,blue,green)
text_rectC5=textC5.get_rect()
text_rectC5.center=(wwidth//2+300,wheight//2+50)
corect5="Corect.George la ucis pe Ion."
gresit5="Gresit.George l-a ucis pe Ion."
#variantaD5
textD5=font1.render(D5,True,blue,green)
text_rectD5=textD5.get_rect()
text_rectD5.center=(wwidth//2-300,wheight//2+150)

#end_question_5




#start_question 6
question6='6.Pe cine iubea Ion cu adevarat? :'
text6=font1.render(question6,True,black,background_color)
text_rect6=text6.get_rect()
text_rect6.center=(wwidth//2,140)
A6="A.Florica"
B6="B.Ana"
C6="C.Mizna"
D6="D.Sorina"
E6="E.Desdemona"
#variantaA6
textA6=font1.render(A6,True,blue,green)
text_rectA6=textA6.get_rect()
text_rectA6.center=(wwidth//2-300,wheight//2+50)
#variantaB6
textB6=font1.render(B6,True,blue,green)
text_rectB6=textB6.get_rect()
text_rectB6.center=(wwidth//2,wheight//2+50)
#variantaC6
textC6=font1.render(C6,True,blue,green)
text_rectC6=textC6.get_rect()
text_rectC6.center=(wwidth//2+300,wheight//2+50)
corect6="Corect.Ion o iubea cu adevarat pe Florica ."
gresit6="Gresit.Ion o iubea cu adevarat pe Florica."
#variantaD6
textD6=font1.render(D6,True,blue,green)
text_rectD6=textD6.get_rect()
text_rectD6.center=(wwidth//2-300,wheight//2+150)
#variantaE6
textE6=font1.render(E6,True,blue,green)
text_rectE6=textE6.get_rect()
text_rectE6.center=(wwidth//2,wheight//2+150)

#end_question_6



#start_question 7
question7='7.Pe cine "iubea" Ion doar pentru avere :'
text7=font1.render(question7,True,black,background_color)
text_rect7=text7.get_rect()
text_rect7.center=(wwidth//2,140)
A7="A.Florica"
B7="B.Ana"
C7="C.Mizna"
D7="D.Sorina"
E7="E.Desdemona"
#variantaA7
textA7=font1.render(A7,True,blue,green)
text_rectA7=textA7.get_rect()
text_rectA7.center=(wwidth//2-300,wheight//2+50)
#variantaB7
textB7=font1.render(B7,True,blue,green)
text_rectB7=textB7.get_rect()
text_rectB7.center=(wwidth//2,wheight//2+50)
#variantaC7
textC7=font1.render(C7,True,blue,green)
text_rectC7=textC7.get_rect()
text_rectC7.center=(wwidth//2+300,wheight//2+50)
corect7="Corect.Ion o iubea pentru bani pe Ana ."
gresit7="Gresit.Ion o iubea pentru bani pe Ana."
#variantaD7
textD7=font1.render(D7,True,blue,green)
text_rectD7=textD7.get_rect()
text_rectD7.center=(wwidth//2-300,wheight//2+150)
#variantaE7
textE7=font1.render(E7,True,blue,green)
text_rectE7=textE7.get_rect()
text_rectE7.center=(wwidth//2,wheight//2+150)

#end_question_7



#start_question 8
question8='8.Tatal Anei se numea :'
text8=font1.render(question8,True,black,background_color)
text_rect8=text8.get_rect()
text_rect8.center=(wwidth//2,140)
A8="A.Florin Plugarul"
B8="B.Mihai Nebunu'"
C8="C.Cizmar Bogdan"
D8="D.Luca Cimitir"
E8="E.Vasile Baciu"
#variantaA8
textA8=font1.render(A8,True,blue,green)
text_rectA8=textA8.get_rect()
text_rectA8.center=(wwidth//2-300,wheight//2+50)
#variantaB8
textB8=font1.render(B8,True,blue,green)
text_rectB8=textB8.get_rect()
text_rectB8.center=(wwidth//2,wheight//2+50)
#variantaC8
textC8=font1.render(C8,True,blue,green)
text_rectC8=textC8.get_rect()
text_rectC8.center=(wwidth//2+300,wheight//2+50)
corect8="Corect.Tatal Anei se numea Vasile Baciu."
gresit8="Gresit.Tatal Anei se numea Vasile Baciu."
#variantaD8
textD8=font1.render(D8,True,blue,green)
text_rectD8=textD8.get_rect()
text_rectD8.center=(wwidth//2-300,wheight//2+150)
#variantaE8
textE8=font1.render(E8,True,blue,green)
text_rectE8=textE8.get_rect()
text_rectE8.center=(wwidth//2,wheight//2+150)

#end_question_8


#start_question 7
question9='9.Cum se numeste tatal lui Ion :'
text9=font1.render(question9,True,black,background_color)
text_rect9=text9.get_rect()
text_rect9.center=(wwidth//2,140)
A9="A.Alexandru Glanetasu"
B9="B.Salam Mircea"
C9="C.Dorel Tenebrosul"
D9="D.Minune Fanica"
E9="E.Irinel Corcodus"
#variantaA9
textA9=font1.render(A9,True,blue,green)
text_rectA9=textA9.get_rect()
text_rectA9.center=(wwidth//2-300,wheight//2+50)
#variantaB9
textB9=font1.render(B9,True,blue,green)
text_rectB9=textB9.get_rect()
text_rectB9.center=(wwidth//2+40,wheight//2+50)
#variantaC9
textC9=font1.render(C9,True,blue,green)
text_rectC9=textC9.get_rect()
text_rectC9.center=(wwidth//2+340,wheight//2+50)
corect9="Corect.Tatal lui Ion se numeste Alexandru Glanetasu."
gresit9="Gresit.Tatal lui Ion se numeste Alexandru Glanetasu."
#variantaD9
textD9=font1.render(D9,True,blue,green)
text_rectD9=textD9.get_rect()
text_rectD9.center=(wwidth//2-300,wheight//2+150)
#variantaE9
textE9=font1.render(E9,True,blue,green)
text_rectE9=textE9.get_rect()
text_rectE9.center=(wwidth//2,wheight//2+150)

#end_question_9



#start_question 10
question10='10.De ce nu il doreste Vasile ca ginere pe Ion :'
text10=font1.render(question10,True,black,background_color)
text_rect10=text10.get_rect()
text_rect10.center=(wwidth//2,140)
A10="A.Provine dintr-o familie saraca"
B10="B.Tatal sau e un betiv"
C10="C.Are probleme cu controlul furiei"
D10="D.Este un pacatos"
E10="E.Petrece prea mult timp la hora"
#variantaA10
textA10=font1.render(A10,True,blue,green)
text_rectA10=textA10.get_rect()
text_rectA10.center=(wwidth//2-100,wheight//2)
#variantaB10
textB10=font1.render(B10,True,blue,green)
text_rectB10=textB10.get_rect()
text_rectB10.center=(wwidth//2-100,wheight//2+50)
#variantaC10
textC10=font1.render(C10,True,blue,green)
text_rectC10=textC10.get_rect()
text_rectC10.center=(wwidth//2-100,wheight//2+100)
corect10="Corect.Pentru ca familia lui Ion e saraca."
gresit10="Gresit.Pentru ca familia lui Ion e saraca."
#variantaD10
textD10=font1.render(D10,True,blue,green)
text_rectD10=textD10.get_rect()
text_rectD10.center=(wwidth//2-100,wheight//2+150)
#variantaE10
textE10=font1.render(E10,True,blue,green)
text_rectE10=textE10.get_rect()
text_rectE10.center=(wwidth//2-100,wheight//2+200)

#end_question_10


while running:
    if question_index==1:
        if flipper:
            window.blit(text1, text_rect1)
            window.blit(textA1, text_rectA1)
            window.blit(textB1, text_rectB1)
            pygame.display.flip()
            flipper=False
    elif question_index==2:
        if flipper:
            window.fill(background_color)
            window.blit(text2, text_rect2)
            window.blit(textA2, text_rectA2)
            window.blit(textB2, text_rectB2)
            window.blit(textC2,text_rectC2)
            pygame.display.flip()
            flipper=False
    elif question_index == 3:
        if flipper:
            window.fill(background_color)
            window.blit(text3, text_rect3)
            window.blit(textA3, text_rectA3)
            window.blit(textB3, text_rectB3)
            window.blit(textC3, text_rectC3)
            pygame.display.flip()
            flipper = False
    elif question_index == 4:
        if flipper:
            window.fill(background_color)
            window.blit(text4, text_rect4)
            window.blit(textA4, text_rectA4)
            window.blit(textB4, text_rectB4)
            window.blit(textC4, text_rectC4)
            pygame.display.flip()
            flipper = False
    elif question_index == 5:
        if flipper:
            window.fill(background_color)
            window.blit(text5, text_rect5)
            window.blit(textA5, text_rectA5)
            window.blit(textB5, text_rectB5)
            window.blit(textC5, text_rectC5)
            window.blit(textD5,text_rectD5)
            pygame.display.flip()
            flipper = False
    elif question_index == 6:
        if flipper:
            window.fill(background_color)
            window.blit(text6, text_rect6)
            window.blit(textA6, text_rectA6)
            window.blit(textB6, text_rectB6)
            window.blit(textC6, text_rectC6)
            window.blit(textD6,text_rectD6)
            window.blit(textE6,text_rectE6)
            pygame.display.flip()
            flipper = False
    elif question_index == 7:
        if flipper:
            window.fill(background_color)
            window.blit(text7, text_rect7)
            window.blit(textA7, text_rectA7)
            window.blit(textB7, text_rectB7)
            window.blit(textC7, text_rectC7)
            window.blit(textD7,text_rectD7)
            window.blit(textE7,text_rectE7)
            pygame.display.flip()
            flipper = False
    elif question_index == 8:
        if flipper:
            window.fill(background_color)
            window.blit(text8, text_rect8)
            window.blit(textA8, text_rectA8)
            window.blit(textB8, text_rectB8)
            window.blit(textC8, text_rectC8)
            window.blit(textD8,text_rectD8)
            window.blit(textE8,text_rectE8)
            pygame.display.flip()
            flipper = False
    elif question_index == 9:
        if flipper:
            window.fill(background_color)
            window.blit(text9, text_rect9)
            window.blit(textA9, text_rectA9)
            window.blit(textB9, text_rectB9)
            window.blit(textC9, text_rectC9)
            window.blit(textD9,text_rectD9)
            window.blit(textE9,text_rectE9)
            pygame.display.flip()
            flipper = False
    elif question_index == 10:
        if flipper:
            window.fill(background_color)
            window.blit(text10, text_rect10)
            window.blit(textA10, text_rectA10)
            window.blit(textB10, text_rectB10)
            window.blit(textC10, text_rectC10)
            window.blit(textD10,text_rectD10)
            window.blit(textE10,text_rectE10)
            pygame.display.flip()
            flipper = False
    elif question_index==11:
        if flipper:
            window.fill(background_color)
            end_background()
            end_text=font1.render(f"Raspunsuri corecte: {nota}/10",True,black,grey)
            end_text_rect=end_text.get_rect()
            end_text_rect.center=(wwidth//2,wheight//2)
            window.blit(end_text,end_text_rect)
            gmail=font2.render("developer gmail: kingambitrap@gmail.com",True,red)
            gmail_rect=gmail.get_rect()
            gmail_rect.center=(wwidth-200,wheight-10)
            window.blit(gmail,gmail_rect)
            pygame.display.flip()



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if question_index==1:
                if event.key==pygame.K_a:
                    window.fill(background_color)
                    raspuns=font1.render(gresit1,True,green,red)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_gresit()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=2
                    flipper=True
                elif event.key==pygame.K_b:
                    nota+=1
                    window.fill(background_color)
                    raspuns = font1.render(corect1, True, green, blue)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_corect()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=2
                    flipper=True

                else:
                    pass
            elif question_index==2:
                if event.key==pygame.K_a:
                    window.fill(background_color)
                    raspuns=font1.render(gresit2,True,green,red)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_gresit()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=3
                    flipper=True
                elif event.key==pygame.K_b:
                    nota+=1
                    window.fill(background_color)
                    raspuns = font1.render(corect2, True, green, blue)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_corect()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=3
                    flipper=True
                elif event.key==pygame.K_c:
                    window.fill(background_color)
                    raspuns = font1.render(gresit2, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 3
                    flipper = True
            elif question_index==3:
                if event.key==pygame.K_a:
                    nota+=1
                    window.fill(background_color)
                    raspuns=font1.render(corect3,True,green,blue)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_corect()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=4
                    flipper=True
                elif event.key==pygame.K_b:
                    window.fill(background_color)
                    raspuns = font1.render(gresit3, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=4
                    flipper=True
                elif event.key==pygame.K_c:
                    window.fill(background_color)
                    raspuns = font1.render(gresit3, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 4
                    flipper = True
            elif question_index==4:
                if event.key==pygame.K_a:
                    window.fill(background_color)
                    raspuns=font1.render(gresit4,True,green,red)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_gresit()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=5
                    flipper=True
                elif event.key==pygame.K_b:
                    window.fill(background_color)
                    raspuns = font1.render(gresit4, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=5
                    flipper=True
                elif event.key==pygame.K_c:
                    nota+=1
                    window.fill(background_color)
                    raspuns = font1.render(corect4, True, green, blue)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_corect()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 5
                    flipper = True
            elif question_index==5:
                if event.key==pygame.K_a:
                    window.fill(background_color)
                    raspuns=font1.render(gresit5,True,green,red)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_gresit()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=6
                    flipper=True
                elif event.key==pygame.K_b:
                    window.fill(background_color)
                    raspuns = font1.render(gresit5, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=6
                    flipper=True
                elif event.key==pygame.K_c:
                    nota+=1
                    window.fill(background_color)
                    raspuns = font1.render(corect5, True, green, blue)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_corect1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 6
                    flipper = True
                elif event.key==pygame.K_d:
                    window.fill(background_color)
                    raspuns = font1.render(gresit5, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 6
                    flipper = True

            elif question_index==6:
                if event.key==pygame.K_a:
                    nota+=1
                    window.fill(background_color)
                    raspuns=font1.render(corect6,True,green,blue)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_corect1()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=7
                    flipper=True
                elif event.key==pygame.K_b:
                    window.fill(background_color)
                    raspuns = font1.render(gresit6, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=7
                    flipper=True
                elif event.key==pygame.K_c:
                    window.fill(background_color)
                    raspuns = font1.render(corect6, True, green,red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 7
                    flipper = True
                elif event.key==pygame.K_d:
                    window.fill(background_color)
                    raspuns = font1.render(gresit6, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 7
                    flipper = True
                elif event.key == pygame.K_e:
                    window.fill(background_color)
                    raspuns = font1.render(gresit6, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 7
                    flipper = True

            elif question_index==7:
                if event.key==pygame.K_a:
                    window.fill(background_color)
                    raspuns=font1.render(gresit7,True,green,red)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_gresit1()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=8
                    flipper=True
                elif event.key==pygame.K_b:
                    nota+=1
                    window.fill(background_color)
                    raspuns = font1.render(corect7, True, green, blue)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_corect1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=8
                    flipper=True
                elif event.key==pygame.K_c:
                    nota+=1
                    window.fill(background_color)
                    raspuns = font1.render(corect7, True, green,red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index =8
                    flipper = True
                elif event.key==pygame.K_d:
                    window.fill(background_color)
                    raspuns = font1.render(gresit7, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 8
                    flipper = True
                elif event.key == pygame.K_e:
                    window.fill(background_color)
                    raspuns = font1.render(gresit7, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 8
                    flipper = True
            #e este corect la 8

            elif question_index==8:
                if event.key==pygame.K_a:
                    window.fill(background_color)
                    raspuns=font1.render(gresit8,True,green,red)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_gresit1()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=9
                    flipper=True
                elif event.key==pygame.K_b:
                    window.fill(background_color)
                    raspuns = font1.render(gresit8, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=9
                    flipper=True
                elif event.key==pygame.K_c:
                    window.fill(background_color)
                    raspuns = font1.render(gresit8, True, green,red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index =9
                    flipper = True
                elif event.key==pygame.K_d:
                    window.fill(background_color)
                    raspuns = font1.render(gresit8, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 9
                    flipper = True
                elif event.key == pygame.K_e:
                    nota+=1
                    window.fill(background_color)
                    raspuns = font1.render(corect8, True, green, blue)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_corect1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 9
                    flipper = True
            elif question_index==9:
                if event.key == pygame.K_a:
                    nota += 1
                    window.fill(background_color)
                    raspuns=font1.render(corect9,True,green,blue)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_corect1()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=10
                    flipper=True

                elif event.key == pygame.K_b:
                    window.fill(background_color)
                    raspuns = font1.render(gresit9, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 10
                    flipper = True
                elif event.key==pygame.K_c:
                    window.fill(background_color)
                    raspuns = font1.render(gresit9, True, green,red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index =10
                    flipper = True
                elif event.key==pygame.K_d:
                    window.fill(background_color)
                    raspuns = font1.render(gresit9, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 10
                    flipper = True
                elif event.key == pygame.K_e:
                    window.fill(background_color)
                    raspuns = font1.render(gresit9, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 10
                    flipper = True

            elif question_index==10:
                if event.key==pygame.K_a:
                    nota+=1
                    window.fill(background_color)
                    raspuns=font1.render(corect10,True,green,blue)
                    raspuns_rect=raspuns.get_rect()
                    raspuns_rect.center=(wwidth//2,wheight//2)
                    background_corect1()
                    window.blit(raspuns,raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=11
                    flipper=True
                elif event.key==pygame.K_b:
                    window.fill(background_color)
                    raspuns = font1.render(gresit10, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index=11
                    flipper=True
                elif event.key==pygame.K_c:
                    window.fill(background_color)
                    raspuns = font1.render(gresit10, True, green,red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index =11
                    flipper = True
                elif event.key==pygame.K_d:
                    window.fill(background_color)
                    raspuns = font1.render(gresit10, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 11
                    flipper = True
                elif event.key == pygame.K_e:
                    window.fill(background_color)
                    raspuns = font1.render(gresit10, True, green, red)
                    raspuns_rect = raspuns.get_rect()
                    raspuns_rect.center = (wwidth // 2, wheight // 2)
                    background_gresit1()
                    window.blit(raspuns, raspuns_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    question_index = 11
                    flipper = True