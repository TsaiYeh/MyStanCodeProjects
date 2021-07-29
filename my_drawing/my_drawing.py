"""
File: my_drawing.py
Name: 吳采曄 Judy Wu
----------------------
During COVID time, draw a 阿中部長 to ask everyone to wash hands, stay at home, and do the SC101 homework.
Hope the COVID situation will become better soon so we can continue the course in person.
As there are too many lines in this program, I separate them into different functions:
background, person (means body), head, speak (words), and table.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GRoundRect, GPolygon, GArc
from campy.graphics.gwindow import GWindow

# Global Variable
window = GWindow(width=800, height=600, title='Covid precaution')


def main():
    """
    During COVID time, draw a 阿中部長 to ask everyone to wash hands, stay at home, and do the SC101 homework.
    Hope the COVID situation will become better soon so we can continue the course in person.
    As there are too many lines in this program, I separate them into different functions:
    background, person (means body), head, speak (words), and table.
    """
    background = GRect(800, 600)
    background.filled = True
    background.fill_color = 'white'
    window.add(background)

    person()
    head()
    speak()
    table()


def head():
    """
    :return: the face, hair, and the facial features of the minister.
    """
    ear1 = GOval(30, 30, x=307, y=130)                      # left ear
    ear1.filled = True
    ear1.fill_color = 'wheat'
    window.add(ear1)

    ear2 = GOval(30, 30, x=463, y=130)                      # right ear
    ear2.filled = True
    ear2.fill_color = 'wheat'
    window.add(ear2)

    # face = GRoundRect(160, 170, x=320, y=50, corner=CORNER_ROUNDING)
    face = GOval(155, 170, x=322.5, y=50)                   # face
    face.filled = True
    face.fill_color = 'wheat'
    window.add(face)

    eyebrow1 = GArc(38, 15, 20, 170, x=350, y=115)          # left eye brow
    window.add(eyebrow1)

    eyebrow2 = GArc(35, 15, 350, 180, x=420, y=115)         # right eye brow
    window.add(eyebrow2)

    eye1 = GOval(30, 8, x=353, y=135)                       # left eye
    # eye1.add_vertex((355, 140))
    # eye1.add_vertex((380, 135))
    # eye1.add_vertex((385, 140))
    eye1.filled = True
    eye1.fill_color = 'white'
    window.add(eye1)

    eyeball1 = GOval(10, 8, x=363, y=135)                   # left eye ball
    eyeball1.filled = True
    eyeball1.fill_color = 'black'
    window.add(eyeball1)

    bling1 = GOval(3, 3, x=365, y=137)                      # the bling bling in the left eye ball
    bling1.filled = True
    bling1.fill_color = 'white'
    window.add(bling1)

    eye1_lower = GArc(40, 20, 245, 120, x=350, y=143)       # the wrinkle under left eye
    window.add(eye1_lower)

    eye2 = GOval(30, 8, x=421, y=135)                       # right eye
    # eye2.add_vertex((425, 140))
    # eye2.add_vertex((430, 135))
    # eye2.add_vertex((455, 140))
    eye2.filled = True
    eye2.fill_color = 'white'
    window.add(eye2)

    eyeball2 = GOval(10, 8, x=430, y=135)                   # right eye ball
    eyeball2.filled = True
    eyeball2.fill_color = 'black'
    window.add(eyeball2)

    bling2 = GOval(3, 3, x=432, y=137)                      # the bling bling in the right eye ball
    bling2.filled = True
    bling2.fill_color = 'white'
    window.add(bling2)

    eye2_lower = GArc(40, 20, 170, 130, x=426, y=143)       # the wrinkle under right eye
    window.add(eye2_lower)

    nose1 = GLine(397, 138, 392, 170)                       # upper part of the nose
    window.add(nose1)

    nose2 = GArc(22, 12, 180, 160, x=392, y=165)            # lower part of the nose
    window.add(nose2)

    # wrinkle1 = GArc(25, 50, 70, 150, x=370, y=165)
    wrinkle1 = GLine(372, 185, 380, 168)                    # left nasolabial pattern
    window.add(wrinkle1)

    # wrinkle2 = GArc(25, 65, 340, 130, x=415, y=165)
    wrinkle2 = GLine(432, 185, 422, 168)                    # right nasolabial pattern
    window.add(wrinkle2)

    mouth = GOval(50, 10, x=375, y=190)                     # mouth
    mouth.filled = True
    mouth.fill_color = 'maroon'
    window.add(mouth)

    mouth_low = GArc(45, 10, 180, 135, x=385, y=200)        # wrinkle under mouth
    window.add(mouth_low)

    hair1 = GPolygon()                                      # hair
    hair1.add_vertex((432, 47))
    hair1.add_vertex((420, 40))
    hair1.add_vertex((400, 35))
    hair1.add_vertex((360, 40))
    hair1.add_vertex((330, 55))
    hair1.add_vertex((320, 70))
    hair1.add_vertex((317, 90))
    hair1.add_vertex((316, 110))
    hair1.add_vertex((320, 140))
    hair1.add_vertex((330, 145))
    hair1.add_vertex((340, 105))
    hair1.add_vertex((360, 95))
    hair1.add_vertex((357, 100))
    hair1.add_vertex((370, 95))
    hair1.add_vertex((368, 100))
    hair1.add_vertex((400, 95))
    hair1.add_vertex((398, 100))
    hair1.add_vertex((415, 93))
    hair1.add_vertex((430, 80))
    hair1.add_vertex((435, 100))
    hair1.add_vertex((438, 95))
    hair1.add_vertex((450, 105))
    hair1.add_vertex((460, 110))
    hair1.add_vertex((465, 120))
    hair1.add_vertex((473, 145))
    hair1.add_vertex((483, 140))
    hair1.add_vertex((490, 120))
    hair1.add_vertex((491, 100))
    hair1.add_vertex((492, 90))
    hair1.add_vertex((490, 80))
    hair1.add_vertex((488, 70))
    hair1.add_vertex((484, 60))
    hair1.add_vertex((480, 55))
    hair1.add_vertex((470, 48))
    hair1.add_vertex((460, 44))
    hair1.add_vertex((445, 46))
    hair1.add_vertex((440, 50))
    hair1.add_vertex((432, 46))
    hair1.filled = True
    hair1.fill_color = 'darkgray'
    window.add(hair1)

    hair_line1 = GLine(375, 95, 400, 86)                # the brighter part of the hair
    hair_line1.color = 'lightgray'
    window.add(hair_line1)
    hair_line2 = GLine(375, 90, 385, 87)
    hair_line2.color = 'lightgray'
    window.add(hair_line2)
    hair_line3 = GLine(340, 100, 370, 85)
    hair_line3.color = 'lightgray'
    window.add(hair_line3)
    hair_line4 = GLine(340, 82, 385, 55)
    hair_line4.color = 'lightgray'
    window.add(hair_line4)
    hair_line5 = GLine(340, 88, 380, 72)
    hair_line5.color = 'lightgray'
    window.add(hair_line5)
    hair_line6 = GLine(340, 95, 375, 78)
    hair_line6.color = 'lightgray'
    window.add(hair_line6)
    hair_line7 = GLine(330, 100, 330, 135)
    hair_line7.color = 'lightgray'
    window.add(hair_line7)
    hair_line8 = GLine(325, 95, 327, 130)
    hair_line8.color = 'lightgray'
    window.add(hair_line8)
    hair_line9 = GLine(435, 75, 440, 90)
    hair_line9.color = 'lightgray'
    window.add(hair_line9)
    hair_line10 = GLine(445, 83, 465, 100)
    hair_line10.color = 'lightgray'
    window.add(hair_line10)
    hair_line11 = GLine(448, 90, 465, 107)
    hair_line11.color = 'lightgray'
    window.add(hair_line11)
    hair_line12 = GLine(472, 105, 478, 132)
    hair_line12.color = 'lightgray'
    window.add(hair_line12)
    hair_line13 = GArc(30, 80, 345, 150, x=450, y=55)
    hair_line13.color = 'lightgray'
    window.add(hair_line13)


def speak():
    """
    :return: the dialog boxes and the words that the minister speaks.
    """
    speak1 = GOval(200, 200, x=50, y=50)                # left dialog box (round part)
    speak1.filled = True
    speak1.fill_color = 'lightsage'
    speak1.color = 'lightsage'
    window.add(speak1)

    speak2 = GPolygon()                                 # left dialog box (tip part)
    speak2.add_vertex((250, 150))
    speak2.add_vertex((200, 200))
    speak2.add_vertex((280, 180))
    speak2.filled = True
    speak2.fill_color = 'lightsage'
    speak2.color = 'lightsage'
    window.add(speak2)

    speak3 = GOval(150, 200, x=600, y=50)               # right dialog box (round part)
    speak3.filled = True
    speak3.fill_color = 'lightsage'
    speak3.color = 'lightsage'
    window.add(speak3)

    speak4 = GPolygon()                                 # right dialog box (tip part)
    speak4.add_vertex((620, 180))
    speak4.add_vertex((650, 240))
    speak4.add_vertex((580, 225))
    speak4.filled = True
    speak4.fill_color = 'lightsage'
    speak4.color = 'lightsage'
    window.add(speak4)

    word1 = GLabel('待 在 家', x=85, y=150)               # speaking words
    word1.font = 'Microsoft JhengHei-28'
    window.add(word1)

    word2 = GLabel('寫 作 業', x=85, y=200)               # speaking words
    word2.font = 'Microsoft JhengHei-28'
    window.add(word2)

    word3 = GLabel('勤', x=655, y=130)                   # speaking words
    word3.font = 'Microsoft JhengHei-28'
    window.add(word3)

    word4 = GLabel('洗', x=655, y=180)                   # speaking words
    word4.font = 'Microsoft JhengHei-30'
    window.add(word4)

    word5 = GLabel('手', x=655, y=230)                   # speaking words
    word5.font = 'Microsoft JhengHei-30'
    window.add(word5)


def person():
    """
    :return: the body of the minister, including clothes, hands, and microphone.
    """
    body = GRoundRect(200, 160, x=300, y=200)               # the gray vest
    body.filled = True
    body.fill_color = 'dimgray'
    window.add(body)

    zipper1 = GRect(8, 20, x=397, y=280)                    # the zipped part
    zipper1.filled = True
    zipper1.fill_color = 'black'
    window.add(zipper1)
    zipper2 = GRect(2.5, 50, x=400, y=300)                  # the zipper
    zipper2.filled = True
    zipper2.fill_color = 'black'
    window.add(zipper2)

    white_cloth = GPolygon()                                # the white cloth
    white_cloth.add_vertex((400, 280))
    white_cloth.add_vertex((480, 200))
    white_cloth.add_vertex((320, 200))
    white_cloth.filled = True
    white_cloth.fill_color = 'white'
    window.add(white_cloth)

    white_collar1 = GPolygon()                              # right collar of the white cloth
    white_collar1.add_vertex((460, 200))
    white_collar1.add_vertex((410, 240))
    white_collar1.add_vertex((430, 250))
    white_collar1.filled = True
    white_collar1.fill_color = 'white'
    window.add(white_collar1)

    white_collar2 = GPolygon()                              # left collar of the white cloth
    white_collar2.add_vertex((340, 200))
    white_collar2.add_vertex((390, 240))
    white_collar2.add_vertex((370, 250))
    white_collar2.filled = True
    white_collar2.fill_color = 'white'
    window.add(white_collar2)

    yellow_collar = GPolygon()                              # the yellow-colored right collar of the vest
    yellow_collar.add_vertex((400, 280))
    yellow_collar.add_vertex((450, 255))
    yellow_collar.add_vertex((465, 265))
    yellow_collar.add_vertex((480, 200))
    yellow_collar.filled = True
    yellow_collar.fill_color = 'yellow'
    window.add(yellow_collar)

    yellow_collar2 = GPolygon()                             # the yellow-colored left collar of the vest
    yellow_collar2.add_vertex((400, 280))
    yellow_collar2.add_vertex((350, 255))
    yellow_collar2.add_vertex((335, 265))
    yellow_collar2.add_vertex((320, 200))
    yellow_collar2.filled = True
    yellow_collar2.fill_color = 'yellow'
    window.add(yellow_collar2)

    neck = GPolygon()                                       # neck
    neck.add_vertex((340, 200))
    neck.add_vertex((390, 240))
    neck.add_vertex((400, 260))
    neck.add_vertex((410, 240))
    neck.add_vertex((460, 200))
    neck.filled = True
    neck.fill_color = 'wheat'
    window.add(neck)

    nhcc = GLabel('NHCC', x=423, y=310)                     # the NHCC wording on the vest
    nhcc.font = 'Microsoft JhengHei-16-bold'
    nhcc.color = 'white'
    window.add(nhcc)

    left_palm = GOval(45, 35, x=511, y=95)                  # left palm
    left_palm.filled = True
    left_palm.fill_color = 'wheat'
    window.add(left_palm)
    left_hand1 = GArc(100, 100, 270, 150, x=475, y=112)     # the lower part of the left arm
    window.add(left_hand1)
    left_hand2 = GArc(200, 230, 260, 140, x=450, y=85)      # the upper part of the left arm
    window.add(left_hand2)
    left_hand3 = GRect(40, 10, x=515, y=120)                # the cuff of the left arm
    left_hand3.filled = True
    left_hand3.fill_color = 'white'
    window.add(left_hand3)

    mc_head = GOval(35, 30, x=360, y=225)                   # the orange part of the microphone
    mc_head.filled = True
    mc_head.fill_color = 'tomato'
    window.add(mc_head)

    mc = GRect(25, 50, x=365, y=250)                        # the grip part of the microphone
    mc.filled = True
    window.add(mc)

    right_palm = GOval(40, 45, x=355, y=280)                # right palm
    right_palm.filled = True
    right_palm.fill_color = 'wheat'
    window.add(right_palm)
    right_hand = GRect(60, 45, x=300, y=280)                # the forearm of the right hand
    right_hand.filled = True
    right_hand.fill_color = 'white'
    window.add(right_hand)
    right_hand2 = GArc(200, 125, 95, 170, x=260, y=200)     # the hind arm of the right hand
    window.add(right_hand2)
    right_hand3 = GLine(300, 280, 300, 325)
    right_hand3.color = 'white'
    window.add(right_hand3)


def table():
    """
    :return: the table including the name card, presentation paper, and cup on the table.
    """
    desk = GRect(400, 150, x=200, y=450)                    # the front side of the table
    desk.filled = True
    desk.fill_color = 'forestgreen'
    window.add(desk)

    desk_upper = GPolygon()                                 # the upper side of the table
    desk_upper.add_vertex((200, 450))
    desk_upper.add_vertex((600, 450))
    desk_upper.add_vertex((550, 350))
    desk_upper.add_vertex((250, 350))
    desk_upper.filled = True
    desk_upper.fill_color = 'forestgreen'
    window.add(desk_upper)

    name_card = GRect(110, 50, x=220, y=380)                # name card
    name_card.filled = True
    name_card.fill_color = 'white'
    window.add(name_card)

    name1 = GLabel('中央流行疫情指揮中心', x=220, y=400)      # the words on the name card
    name1.font = 'Microsoft JhengHei-8'
    window.add(name1)
    name2 = GLabel('陳時中', x=230, y=428)                 # the words on the name card
    name2.font = 'Microsoft JhengHei-14-Bold'
    window.add(name2)
    name3 = GLabel('指揮官', x=290, y=428)                 # the words on the name card
    name3.font = 'Microsoft JhengHei-8'
    window.add(name3)

    paper = GPolygon()                                    # the paper on the table
    paper.add_vertex((385, 360))
    paper.add_vertex((380, 430))
    paper.add_vertex((440, 430))
    paper.add_vertex((435, 360))
    paper.filled = True
    paper.fill_color = 'wheat'
    window.add(paper)

    paper_line1 = GLine(394, 370, 426, 370)               # the words on the paper, shown as lines.
    window.add(paper_line1)
    paper_line2 = GLine(393, 380, 427, 380)
    window.add(paper_line2)
    paper_line3 = GLine(392, 390, 428, 390)
    window.add(paper_line3)
    paper_line4 = GLine(391, 400, 429, 400)
    window.add(paper_line4)
    paper_line5 = GLine(390, 410, 430, 410)
    window.add(paper_line5)
    paper_line6 = GLine(390, 420, 430, 420)
    window.add(paper_line6)

    cup_hand = GOval(20, 20, x=525, y=400)                  # the larger part of the cup grip
    cup_hand.filled = True
    cup_hand.fill_color = 'lightblue'
    window.add(cup_hand)

    cup_hand2 = GOval(15, 15, x=525, y=402.5)               # the smaller part of the cup grip
    cup_hand2.filled = True
    cup_hand2.fill_color = 'forestgreen'
    window.add(cup_hand2)

    cup = GRect(35, 40, x=500, y=390)                       # the cup
    cup.filled = True
    cup.fill_color = 'lightblue'
    window.add(cup)

    cup_upper = GOval(35, 15, x=500, y=380)                 # the mouth of the cup
    cup_upper.filled = True
    cup_upper.fill_color = 'lightblue'
    window.add(cup_upper)


if __name__ == '__main__':
    main()
