import time

from tkinter import *

digi_clock = Tk()
digi_clock.title('Digital Clock')
digi_clock.geometry('625x785')
#digi_clock.resizable(0,0)

clock_font = ('Optima',40,'bold')

# color codes: https://www.color-hex.com/

fg_clock = '#424141'
bg_clock = '#000000'
active_clock = '#d7d8cc'  #eeeeee för vit
border_width = 20

fg_clock = '#2a2a2a'
# fg_clock = '#000000'


clocktext_without_spaces = '''
KLOCKANTÄRK
FEMYISTIONI
KVARTQIENZO
TJUGOLIVIPM
ÖVERKAMHALV
ETTUSVLXTVÅ
TREMYKYFYRA
FEMSFLORSEX
SJUÅTTAINIO
TIOELVATOLV
'''

clocktext=' '.join([letter for letter in clocktext_without_spaces])

print((clocktext))

def numbertoindex(hour,minute):
    indexes=[]
    KLOCKAN = ['2.1','2.14']
    indexes.append(KLOCKAN)
    ÄR=['2.17','2.20']
    indexes.append(ÄR)

    if hour==12:
        hour=0

    ### MINUTER ###

    m_1=['3.1','3.7'] # 5-9 över säger att klockan är fem över. FEM
    m_2=['3.12','3.18'] # TIO
    m_3=['4.1','4.11'] # KVART
    m_4=['5.1','5.11'] # TJUGO
    m_5=m_1 # FEM
    m_6=['6.14','6.23'] # HALV
    m_7=m_1 # FEM
    m_8=m_4 # TJUGO
    m_9=m_3 # KVART
    m_10=m_2 # TIO
    m_11=m_1 # FEM

    try:
        indexes.append(locals()['m_'+str(minute//5)])
    except:
        None

    I_1=['3.9','3.11']
    I_2=['3.20','3.23']
    I_3=['4.12','4.14']
    I_4=['5.12','5.14']
    ÖVER=['6.1','6.9']


    if minute // 5 in [1,2,3,4]:
        indexes.append(ÖVER)
    elif minute // 5 == 5:
        indexes.append(I_1)
        indexes.append(m_6)
    elif minute // 5 == 7:
        indexes.append(ÖVER)
        indexes.append(m_6)
    elif minute // 5 in [8,9,10,11]:
        indexes.append(locals()['I_'+str(12-minute//5)])


    ### TIMMAR ###

    h_0=['11.15','11.23']
    h_1 = ['7.1','7.7']
    h_2=['7.17','7.23']
    h_3=['8.1','8.7']
    h_4=['8.15','8.23']
    h_5=['9.1','9.7']
    h_6=['9.17','9.23']
    h_7=['10.1','10.7']
    h_8=['10.7','10.15']
    h_9=['10.17','10.23']
    h_10=['11.1','11.7']
    h_11=['11.7','11.15']

    for hour_index in range(0,12):
        if hour == hour_index:
            if minute < 25:
                indexes.append(locals()['h_'+str(hour_index)])
            elif hour == 11:
                indexes.append(h_0)
            else:
                indexes.append(locals()['h_'+str(hour_index+1)])
    
    return indexes

clock_text = Text(digi_clock, font=clock_font, fg=fg_clock,bg=bg_clock, bd=border_width)

clock_text.insert(INSERT, clocktext)
clock_text.grid(row=0,column=0)


def digital_clock():
    clock_text.delete('1.1','12.24')
    clock_text.insert(INSERT, clocktext)
    time_local = time.strftime('%I %M %S')  #Ger en string där man kan hämta tiden med %-grejerna, 12h-klocka.
    [hour,minute,second] = time_local.split() #Lista med strings
    active_words_indexes = numbertoindex(int(hour),int(minute)) # Lista med index på formen 'rad kolumn'

    for indexes in active_words_indexes:
        clock_text.tag_add('tag', indexes[0], indexes[1])
        clock_text.tag_config('tag', foreground=active_clock)
    
    #print(f'{hour}:{minute}:{second}')
    
    clock_text.after(1000, digital_clock)


digital_clock()

digi_clock.mainloop()