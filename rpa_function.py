# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:49:26 2021

@author: michael
"""
import pyautogui
import time
import os
import pandas as pd

def redCircleLoc():
    i = 0 
    loc = []
    for i in range(5):
        red  = pyautogui.locateAllOnScreen('./image/circles-9px/red{}.png'.format(i), grayscale=False, confidence = 0.7)
        for x in red:
            move_mouse = pyautogui.moveTo(x)
            print(x)
            #time.sleep(0.25)
            loc.append(x)
            
    blue_df = pd.DataFrame(loc, columns = ['x', 'y', 'w', 'h'])
    blue_df.sort_values(by = ['y'])
    
    x_space = []
    i =0
    for i in range(len(blue_df['x'])):
        last = len(blue_df['x']) - 1
        if i == len(blue_df['x']) or i == last:
            x_space.append(7)
        else:
            diff_x = abs(blue_df['x'][i+1] - blue_df['x'][i])
            x_space.append(diff_x)
        i+=1
    print('x_space: ', x_space)
    index_exempted = []
    for i in range(len(x_space)):
        if x_space[i] < 2:
            index_exempted.append(i)
        else:
            pass
    print('INDEX EXEMPTED: ', index_exempted)
    for ex in index_exempted:
        yi = blue_df['y'][ex]
        yii = blue_df['y'][ex+1]
        xi = blue_df['x'][ex]
        xii = blue_df['x'][ex+1]
        if yii - yi < 2:
            blue_df = blue_df.drop([ex])
        else:
            pass
        
    blue_df = blue_df.sort_values(by = ['y', 'x'])
    blue_df = blue_df.reset_index()
    print('DF RED 1ST : ', blue_df)
    #df_red = df_red.drop_duplicates(subset = ['y', 'x'], keep = 'first', inplace = True)
    #print('DF RED 2nd : ', df_red)
    df_red_x = []
    df_red_y = []
    j = 0
    for j in range(len(blue_df['x'])):
        df_red_x.append(blue_df['x'][j])
        df_red_y.append(blue_df['y'][j])
        j+=1
    
    return df_red_x, df_red_y


def blueCircleLoc():
    i = 0
    loc = []
    for i in range(5):
        red  = pyautogui.locateAllOnScreen('./image/circles-9px/blue{}.png'.format(i), grayscale=False, confidence = 0.7)
        for x in red:
            move_mouse = pyautogui.moveTo(x)
            print(x)
            #time.sleep(0.25)
            loc.append(x)
            
    blue_df = pd.DataFrame(loc, columns = ['x', 'y', 'w', 'h'])
    blue_df = blue_df.sort_values('y')

    x_space = []
    i =0
    for i in range(len(blue_df['x'])):
        last = len(blue_df['x']) - 1
        if i == len(blue_df['x']) or i == last:
            x_space.append(7)
        else:
            diff_x = abs(blue_df['x'][i+1] - blue_df['x'][i])
            x_space.append(diff_x)
        i+=1
    print('x_space: ', x_space)
    index_exempted = []
    for i in range(len(x_space)):
        if x_space[i] < 2:
            index_exempted.append(i)
        else:
            pass
    print('INDEX EXEMPTED: ', index_exempted)
    for ex in index_exempted:
        yi = blue_df['y'][ex]
        yii = blue_df['y'][ex+1]
        xi = blue_df['x'][ex]
        xii = blue_df['x'][ex+1]
        if yii - yi < 2:
            blue_df = blue_df.drop([ex])
        else:
            pass
    
    blue_df = blue_df.sort_values(by = ['y', 'x'])
    blue_df = blue_df.reset_index()
    print('blue_df: ', blue_df)
    df_blue_x = []
    df_blue_y = []
    j = 0
    for j in range(len(blue_df['x'])):
        df_blue_x.append(blue_df['x'][j])
        df_blue_y.append(blue_df['y'][j])
        j+=1
    
    return df_blue_x, df_blue_y



def nearBtn(con_seq, plist_btn):
    dist = []
    print('plist_btn: ', plist_btn)
    print('con_seq: ', con_seq)
    for d in plist_btn:
        diff_d = abs(int(d) - int(con_seq))
        dist.append(diff_d)
        print('kelz: ', diff_d)
    i_min_dist = min(dist)
    i = dist.index(i_min_dist)
    return i

# def bet(blue, plist_btn, p_btn_loc, amountbet_Btn):
#     dict_amount = {1:50, 2:75, 3:200, 4:500, 5:900, 6:2000, 7:5000}
#     try:
#         for b in blue:
#             amount = dict_amount[b[0]]
#             y_con = b[2]
#             if b[2] < plist_btn[1]:
#                 placeBtn = p_btn_loc[0]
#             elif p_btn_loc[1] < b[2] < p_btn_loc[2]:
#                 placeBtn = p_btn_loc[1]
#             else:
#                 placeBtn = p_btn_loc[2]
#             bet = rf.betAmount(amount, amountbet_Btn, placeBtn)
#     except:
#         pass
    

# def betAmount(amount, loc_betBtn, place_bet_btn):
#     if amount < 7:
#         IMAGE_PATH = './image'
#         TOKEN_BTN = ['10tk.png', '50tk.png', '250tk.png', '500tk.png', '1000tk.png', '5000tk.png']
#         click_bet = pyautogui.click(loc_betBtn)
#         loc_1 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[0]) , grayscale=True,  confidence = 1)
#         loc_5 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[1]) , grayscale=True,  confidence = 1)
#         loc_25 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[2]) , grayscale=True,  confidence = 1)
#         loc_50 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[3]) , grayscale=True,  confidence = 1)
#         loc_100 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[4]) , grayscale=True,  confidence = 1)
#         loc_500 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[5]) , grayscale=True,  confidence = 1)
#         time.sleep(3)
#         if amount == 50:
#             #pyautogui.click(loc_betBtn)
#             pyautogui.moveTo(loc_50)
#             time.sleep(1)
#             pyautogui.click(loc_50)
#             pyautogui.click(place_bet_btn)
#             pyautogui.alert('SUCCESSFULLY PLACE BET OF {}'.format(amount))
#         elif amount == 75:
#             #pyautogui.click(loc_betBtn)
#             pyautogui.moveTo(loc_50)
#             time.sleep(1)
#             pyautogui.click(loc_50)
#             time.sleep(1)
#             pyautogui.click(place_bet_btn)
#             pyautogui.click(loc_betBtn)
#             pyautogui.moveTo(loc_25)
#             time.sleep(1)
#             pyautogui.click(loc_25)
#             time.sleep(1)
#             pyautogui.click(place_bet_btn)
#             pyautogui.alert('SUCCESSFULLY PLACE BET OF {}'.format(amount))
#         elif amount == 200:
#             pyautogui.moveTo(loc_100)
#             time.sleep(1)
#             pyautogui.click(loc_100)
#             time.sleep(1)
#             pyautogui.click(place_bet_btn)
#             pyautogui.click(place_bet_btn)
#             pyautogui.alert('SUCCESSFULLY PLACE BET OF {}'.format(amount))
#         elif amount == 900:
#             pyautogui.moveTo(loc_500)
#             time.sleep(1)
#             pyautogui.click(loc_500)
#             time.sleep(1)
#             pyautogui.click(place_bet_btn)
#             pyautogui.click(loc_betBtn)
#             pyautogui.click(loc_100)
#             time.sleep(1)
#             i = 0
#             for i in range(5):
#                 pyautogui.click(place_bet_btn)
#                 i += 1
#             pyautogui.alert('SUCCESSFULLY PLACE BET OF {}'.format(amount))
#         elif amount == 2000:
#             pyautogui.moveTo(loc_500)
#             time.sleep(1)
#             pyautogui.click(loc_500)
#             time.sleep(1)
#             i = 0
#             for i in range(4):
#                 pyautogui.click(place_bet_btn)
#                 i += 1
#             pyautogui.alert('SUCCESSFULLY PLACE BET OF {}'.format(amount))
#         elif amount == 5000:
#             pyautogui.moveTo(loc_500)
#             time.sleep(1)
#             pyautogui.click(loc_500)
#             time.sleep(1)
#             i = 0
#             for i in range(11):
#                 pyautogui.click(place_bet_btn)
#                 i+=1 
#             pyautogui.alert('SUCCESSFULLY PLACE BET OF {}'.format(amount))
#     else:
#         pass
        
        
def HorizontalCombi(loc_x, loc_y):
    i = 0
    m = []
    #y_condi = []
    for i in range(len(loc_x)):
        try:
            if loc_y[i] == loc_y[i+1]:
                diff = abs(loc_x[i+1] - loc_x[i])
                print('DIFFERENCE: ', diff)
                if diff > 4 and diff < 9:
                    pyautogui.moveTo(loc_x[i], loc_y[i])
                    #pyautogui.alert('CONDITION HAVE MET!!!!')
                    m.append([loc_x[i], loc_y[i]])
                    #y_condi.append(blue_loc_y[i])
                else:
                    pass
            else:
                pass
        except:
            pass
        i+=1
    if len(m) != 0:
        df_m = pd.DataFrame(m, columns =['x', 'y'])
        hoz_condi = []
        print(df_m)
        for y in df_m['y'].unique():
            df_y = df_m[df_m['y'] == y]
            df_y = df_y.reset_index()
            print('DF: ', df_y)
            num_circle_hor = len(df_y['y'].tolist()) + 1
            coor = [num_circle_hor, df_y['x'][0], df_y['y'][0]]
            pyautogui.moveTo(df_y['x'][0], df_y['y'][0])
            hoz_condi.append(coor)
            #pyautogui.alert('CONDITION HAVE MET: {} HORIZONTAL CIRCLE!!!!'.format(num_circle_hor))
        
        
        return hoz_condi
    else:
        #pyautogui.alert('NO CONDITION HAVE MET: 0 HORIZONTAL CIRCLE!!!!')
        pass
        
def verticalCombi(x, y):
    blue_v = pd.DataFrame(list(zip(x, y)), columns = ['x', 'y'])
    blue_v = blue_v.sort_values('x')
    combi = []
    for x_u in blue_v['x'].unique():
        x = blue_v[blue_v['x'] == x_u]
        x = x.drop_duplicates(subset = ['y', 'x'], keep = 'first').sort_values('y').reset_index()
        i = 0
        x_diff = []
        for i in range(len(x['y'])):
            last_num = len(x['y']) - 1
            if i == last_num:
                print(0)
                x_diff.append(0)
            else:
                diff_x = abs(x['y'][i+1] - x['y'][i])
                print(diff_x)
                x_diff.append(diff_x)
            i+=1
            
        index_x = []
        j = 0
        for j in range(len(x_diff)):
            if x_diff[j] > 50 or x_diff[j] < 6:
                pass
            else:
               index_x.append(j)
            j +=1
        
        num_combi = len(index_x) + 1
        if num_combi == 6:
            v_combi = [1, x['x'][index_x[-1]], x['y'][index_x[-1]]]
            pyautogui.moveTo(v_combi[1], v_combi[2])
            #pyautogui.alert('VERTICAL 6 CIRCLE COMBINATION')
            print(v_combi)
            combi.append(v_combi)
        else:
            pass
    print('vertical combination: ', combi)
    return combi

def CleanRepetativeVertical(red_ver_data):
    ##Filtering the repetitive data at vertical
    df_x_f = pd.DataFrame(red_ver_data, columns = ['num', 'x', 'y'])
    df_x_f = df_x_f.sort_values('x')
    i = 0

    d_x = []
    for i in range(len(df_x_f['x'])):
        try:
            last = len(df_x_f['x']) - 1
            boundary = df_x_f['x'][i+1]  - df_x_f['x'][i]
            if i == last:
                d_x.append(7)
                print(7)
            else:
                d_x.append(boundary)
                print(boundary)
        except:
            d_x.append(0)
        i+=1

    clean_data_ver = []
    for k in range(len(d_x)):
        if k != (len(d_x)-1):
            if d_x[k] > 3:
                clean_data_ver.append([df_x_f['num'][k], df_x_f['x'][k], df_x_f['y'][k]])
            else:
                pass
        else:
            if d_x[len(d_x)-1] < 4:
                clean_data_ver.append([df_x_f['num'][k], df_x_f['x'][k], df_x_f['y'][k]])
            else:
                pass
    return clean_data_ver


def CleanRepetativeHorizontal(red_ver_data):
    ##Filtering the repetitive data at vertical
    df_x_f = pd.DataFrame(red_ver_data, columns = ['num', 'x', 'y'])
    df_x_f = df_x_f.sort_values('y')
    i = 0

    d_x = []
    for i in range(len(df_x_f['y'])):
        try:
            last = len(df_x_f['y']) - 1
            boundary = df_x_f['y'][i+1]  - df_x_f['y'][i]
            if i == last:
                d_x.append(7)
                print(7)
            else:
                d_x.append(boundary)
                print(boundary)
        except:
            d_x.append(0)
        i+=1

    clean_data_ver = []
    for k in range(len(d_x)):
        if k != (len(d_x)-1):
            if d_x[k] > 3:
                clean_data_ver.append([df_x_f['num'][k], df_x_f['x'][k], df_x_f['y'][k]])
            else:
                pass
        else:
            if d_x[len(d_x)-1] < 4:
                clean_data_ver.append([df_x_f['num'][k], df_x_f['x'][k], df_x_f['y'][k]])
            else:
                pass
    return clean_data_ver


def betAmount(amount_data, loc_betBtn, place_bet_btn):
    IMAGE_PATH = './image'
    TOKEN_BTN = ['10tk.png', '50tk.png', '250tk.png', '500tk.png', '1000tk.png', '5000tk.png']
    click_bet = pyautogui.click(loc_betBtn)
    loc_10 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[0]) , grayscale=True,  confidence = 1)
    loc_50 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[1]) , grayscale=True,  confidence = 1)
    loc_250 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[2]) , grayscale=True,  confidence = 1)
    loc_500 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[3]) , grayscale=True,  confidence = 1)
    loc_1000 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[4]) , grayscale=True,  confidence = 1)
    loc_5000 = pyautogui.locateOnScreen('{}/{}'.format(IMAGE_PATH, TOKEN_BTN[5]) , grayscale=True,  confidence = 1)
    TOKEN_LOC = [loc_10, loc_50, loc_250, loc_500, loc_1000, loc_5000]
    time.sleep(3)
    i = 0
    for i in range(len(amount_data)):
        if amount_data[i] == 0:
            pass
        else:
            click_bet
            token = pyautogui.moveTo(TOKEN_LOC[i])
            time.sleep(1)
            token = pyautogui.click(TOKEN_LOC[i])
            k = 0
            for k in range(amount_data[i]):
                pyautogui.moveTo(place_bet_btn)
                time.sleep(1)
                put_bet = pyautogui.click(place_bet_btn)
        i+=1
            
            
    
    
    
    
    
    