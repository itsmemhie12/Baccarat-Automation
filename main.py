# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:43:47 2021

@author: michael
"""

import pyautogui
import time
import keyboard
import rpa_function as rf
import os
import pandas as pd
import sys
import cv2


def run(input_data):
    ##########################################  BET AMOUNT #############################################
    INPUT_FILE = input_data
    bet_settings = pd.read_excel(INPUT_FILE)
    bet_settings = bet_settings[bet_settings['to_run'] == 'yes']
    print(bet_settings)
    i = 0
    #list_amount = []
    dict_amount = {}
    for i in range(len(bet_settings['combination'])):
        tk_10 = bet_settings['10tk'][i]
        tk_50 = bet_settings['50tk'][i]
        tk_250 = bet_settings['250tk'][i]
        tk_500 = bet_settings['500tk'][i]
        tk_1000 = bet_settings['1000tk'][i]
        tk_5000 = bet_settings['5000tk'][i]
        #list_amount.append([tk_10, tk_50, tk_250, tk_500, tk_1000, tk_5000])
        dict_amount[bet_settings['combination'][i]] = [tk_10, tk_50, tk_250, tk_500, tk_1000, tk_5000]
        i+=1
    
    
    ##############################  STORING OF ALL COORDINATES OF BUTTON #################################
    time.sleep(2)
    move_mouse = pyautogui.click(108,46)
    amountbet_Btn = pyautogui.locateOnScreen('./image/bettingAmount_btn.png',grayscale=False,  confidence = 0.7)
    move_mouse = pyautogui.moveTo(amountbet_Btn)
    time.sleep(2)
    
    while True:
        #### PLAYER BUTTON FOR PLACING BET
        p_btn_loc = []
        for p_btn in pyautogui.locateAllOnScreen('./image/player_btn-REAL-v2.png', grayscale=False,  confidence = 0.9):
            print(p_btn)
            p_btn_loc.append(p_btn)
            time.sleep(1)
            pyautogui.moveTo(p_btn)
            
        df_p = pd.DataFrame(p_btn_loc, columns = ['x','y','w','h'])
        df_p = df_p.drop_duplicates(['y'], keep ='first')
        df_p = df_p.reset_index()
        
        plist_btn = [y for y in df_p['y'].tolist()]
        print(plist_btn)
        #### BANKER BUTTON FOR PLACING BET
        
        b_btn_loc = []
        for b_btn in pyautogui.locateAllOnScreen('./image/banker_btn-REAL-v2.png', grayscale=False,  confidence = 0.9):
            print(b_btn)
            b_btn_loc.append(b_btn)
            time.sleep(1)
            pyautogui.moveTo(b_btn)
            
        df_b = pd.DataFrame(b_btn_loc , columns = ['x','y','w','h'])
        df_b = df_b.drop_duplicates(['y'], keep ='first')
        df_b = df_b.reset_index()
            
        blist_btn = [y for y in df_b['y'].tolist()]
        
        a = pyautogui.confirm(text='DOES THE PLACE BET BUTTON IS CORRECT?', title='', buttons=['OK', 'RESET'])
    
        if a == 'OK':
            break
        else:
            pass
        
            
    # ##############################  STORING OF ALL COORDINATES OF BUTTON #################################
    try:
        while True:
            #GET CIRCLE LOCATION
            red_loc = rf.redCircleLoc()
            blue_loc = rf.blueCircleLoc()
            #REMOVED DUPLICATE LOCATION
            red_hoz_data = rf.HorizontalCombi(red_loc[0], red_loc[1])
            blue_hoz_data = rf.HorizontalCombi(blue_loc[0], blue_loc[1])
            blue_ver_data = rf.verticalCombi(blue_loc[0], blue_loc[1])
            red_ver_data = rf.verticalCombi(red_loc[0], red_loc[1])
            #GET THE SPECIFIED COMBINATION
            red_hoz_final_data = rf.CleanRepetativeHorizontal(red_hoz_data)
            blue_hoz_final_data = rf.CleanRepetativeHorizontal(blue_hoz_data)
            red_ver_final_data = rf.CleanRepetativeVertical(red_ver_data)
            blue_ver_final_data = rf.CleanRepetativeVertical(blue_ver_data)
            #CONCATENATE THE DETECTED COMBINATION
            blue = blue_ver_final_data + blue_hoz_final_data
            print('BLUE ALL COMBI DATA: ', blue)
            red = red_ver_final_data + red_hoz_final_data
            print('RED ALL COMBI DATA: ', red)
            #RUN PLACING BET
            #dict_amount = {1:50, 2:75, 3:200, 4:500, 5:900, 6:2000, 7:5000}
            try:
                for b in blue:
                    try:
                        amount = dict_amount[b[0]]
                        b_distance = []
                        i = 0
                        for i in range(len(blist_btn)):
                            d = abs(blist_btn[i] - b[2])
                            b_distance.append(d)
                            i += 1
                        k = 0
                        for k in range(len(b_distance)):
                            try:
                                if b_distance[k] < b[2] < b_distance[k+1]:
                                    placeBtn_index = pyautogui.moveTo(b_btn_loc[k])
                                    #pyautogui.alert('combinatin: {}'.format(b[0]))
                                    #print('combinatin: {}'.format(b[0]))
                                    rf.betAmount(amount, amountbet_Btn, b_btn_loc[k])
                                else:
                                    pass
                            except:
                                if b[2] > b_distance[k]:
                                    placeBtn_index = pyautogui.moveTo(b_btn_loc[k])
                                    #pyautogui.alert('combinatin: {}'.format(b[0]))
                                    #print('combinatin: {}'.format(b[0]))
                                    rf.betAmount(amount, amountbet_Btn, b_btn_loc[k])
                            else:
                                pass
                    except:
                        pass
            except:
                pass
            
            try:
                for p in red:
                    try:
                        pamount = dict_amount[b[0]]
                        p_distance = []
                        i = 0
                        for i in range(len(plist_btn)):
                            d = abs(plist_btn[i] - b[2])
                            p_distance.append(d)
                            i += 1
                        k = 0
                        for k in range(len(p_distance)):
                            try:
                                if p_distance[k] < p[2] < p_distance[k+1]:
                                    placeBtn_index = pyautogui.moveTo(p_btn_loc[k])
                                    #pyautogui.alert('combinatin: {}'.format(b[0]))
                                    #print('combinatin: {}'.format(b[0]))
                                    rf.betAmount(pamount, amountbet_Btn, p_btn_loc[k])
                                else:
                                    pass
                            except:
                                if b[2] > b_distance[k]:
                                    placeBtn_index = pyautogui.moveTo(p_btn_loc[k])
                                    #pyautogui.alert('combinatin: {}'.format(b[0]))
                                    #print('combinatin: {}'.format(b[0]))
                                    rf.betAmount(pamount, amountbet_Btn, p_btn_loc[k])
                            else:
                                pass
                    except:
                        pass
            except:
                pass
            
            refresh = pyautogui.locateOnScreen('./image/refresh.png', grayscale=False,  confidence = 0.8)
            pyautogui.click(refresh)
            time.sleep(5)
            pyautogui.FAILSAFE = False
    except KeyboardInterrupt:
        pyautogui.alert('RPA SHUTINGDOWN!!!')
