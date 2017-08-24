# -*- coding: utf-8 -*-
import config
import utils
import socket
import re
import time
import thread
import random
import requests
import datetime
from pytils import translit
from time import sleep
#6 слов в списке(массив)
words = ["сережа","broodmother","thedukentre","moobot","модеры","балтика"]

ho4y = "string"

def main():
    winner = 0
    game = 0
    popitka = 0
    random_word = 0
    sek = 0
    timebot = 0
    randomtime = 0
    game_timer = 0
    ukraine_cooldawn = 0
    baltika_timer = 0
    mmr_timer = 0
    piska_timer = 0
    pogoda_timer = 0
    voteban_timer = 0
    mmr_file = open("mmr_set.txt", "r")
    mmr_set = mmr_file.read()
    mmr_file.close()
    s = socket.socket()
    s.connect((config.HOST, config.PORT))
    s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(config.CHAN).encode("utf-8"))

    chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    utils.mess(s, "Я опять здесь KonCha")

    thread.start_new_thread(utils.fillOpList, ())
    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = chat_message.sub("", response)
            print(response)

            timebot = timebot + 1
            if timebot == 35:
                timebot = 0
            print (timebot)
            if game_timer > 0:
                game_timer = game_timer - 1
            if ukraine_cooldawn > 0:
                ukraine_cooldawn = ukraine_cooldawn - 1
            if baltika_timer > 0:
                baltika_timer = baltika_timer - 1
            if mmr_timer > 0:
                mmr_timer = mmr_timer - 1
            if piska_timer > 0:
                piska_timer = piska_timer - 1
            if pogoda_timer > 0:
                pogoda_timer = pogoda_timer - 1
            if voteban_timer > 0:
                voteban_timer = voteban_timer - 1
            soob = re.search("!mmr_set",message)
            if len(str(soob))>5:
                if username == "thedukentre":
                    check_mmr = re.findall(r"\w*", message)
                    mmr_set = check_mmr[3]
                    print(check_mmr[3])
                    print(mmr_set)
                    mmr_file = open("mmr_set.txt", "w")
                    mmr_file.write(mmr_set)
                    mmr_file.close()
                    mmr_file = open("Debug.txt","a")
                    mmr_file.write(username + " "+mmr_set)
                    mmr_file.close()
                    continue
                elif username == "serejaperviy":
                    check_mmr = re.findall(r"\w*", message)
                    mmr_set = check_mmr[3]
                    print(check_mmr[3])
                    print(mmr_set)
                    mmr_file = open("mmr_set.txt", "w")
                    mmr_file.write(mmr_set)
                    mmr_file.close()
                    mmr_file = open("Debug.txt", "a")
                    mmr_file.write(username + " " + mmr_set)
                    mmr_file.close()
                    continue
                elif username == "liloviy_yoj":
                    check_mmr = re.findall(r"\w*", message)
                    mmr_set = check_mmr[3]
                    print(check_mmr[3])
                    print(mmr_set)
                    mmr_file = open("mmr_set.txt", "w")
                    mmr_file.write(mmr_set)
                    mmr_file.close()
                    mmr_file = open("Debug.txt", "a")
                    mmr_file.write(username + " " + mmr_set)
                    mmr_file.close()
                    continue
                elif utils.isOp(username):
                    check_mmr = re.findall(r"\w*", message)
                    mmr_set = check_mmr[3]
                    print(check_mmr[3])
                    print(mmr_set)
                    mmr_file = open("mmr_set.txt", "w")
                    mmr_file.write(mmr_set)
                    mmr_file.close()
                    mmr_file = open("Debug.txt", "a")
                    mmr_file.write(username + " " + mmr_set)
                    mmr_file.close()
                    continue
            ho4y = re.search(r"!ho4y", message)
            if len(str(ho4y)) > 6:
                utils.mess(s, "Ваше пожелание будет учтено!")
                print(message)
                message.encode("utf-8")
                file_1 = open("ho4y.txt", "a")
                trans = translit.translify(message)
                file_1.write(trans)
                file_1.close()
                ho4y = "ho4y"
                continue
            if message.strip() == "!time":
                utils.mess(s, "Текущее время: " + time.strftime("%I:%M %p %Z on %A %B %d %Y"))
                continue
            soob = re.search("!timeout",message)
            if len(str(soob))>5:
                if username == "thedukentre":
                    timeout = re.findall(r"\w*", message)
                    utils.timeout(s,timeout[3],100)
                    continue
            soob = re.search("!voteban", message)
            if len(str(soob))> 5:
                banned = re.findall(r"\w*", message)
                if voteban_timer == 0:
                    if len(banned[3]) < 3:
                        utils.privat(s,username,"!voteban [ник] , ник пишется без скобок []!")
                    else:
                        ban_time = 0
                        ban_yes = 0
                        ban_no = 0
                        ban_soob = 0
                        playerlist = ["serejaperviy"]

                        utils.mess(s,str(username)+" SwiftRage запустил голосование за таймаут " +str(banned[3])+" SwiftRage . Если вы согласны пишите Да, иначе Нет")
                        while ban_time < 20:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)
                            soob = re.search(u"Да|да",message)
                            if len(str(soob))>4:
                                if str(username) not in playerlist:
                                    ban_yes = ban_yes+1
                                    playerlist.append(str(username))
                            soob = re.search(u"Нет|нет",message)
                            if len(str(soob)) > 4:
                                if str(username) not in playerlist:
                                    ban_no = ban_no + 1
                                    playerlist.append(str(username))
                            ban_soob = ban_soob+1
                            if ban_soob == 3:
                                ban_soob = 0
                                utils.mess(s,"SwiftRage Голосов за: "+str(ban_yes)+" BibleThump Голосов против: "+str(ban_no))
                            ban_time = ban_time+1
                        if ban_yes > ban_no*2:
                            utils.mess(s,"Голосование завершено! Голосов за: "+str(ban_yes)+" Голосов против: "+str(ban_no))
                            utils.mess(s,"SwiftRage SwiftRage "+str(banned[3])+" БУДЕТ ЗАБАНЕН НА 60 СЕКУНД SwiftRage SwiftRage ")
                            utils.timeout(s,banned[3],60)
                        else:
                            utils.mess(s, "Голосование завершено! Голосов за: " + str(ban_yes) + " Голосов против: " + str(ban_no))
                            utils.mess(s, "BibleThump BibleThump " + str(banned[3]) + " БУДЕТ ПОЩЯЖЕН BibleThump BibleThump ")
                        voteban_timer = 300
                        continue
                else:
                    utils.privat(s,username,"До !voteban осталось "+str(voteban_timer)+" сек")
            if message.strip() == "!privat_test":
                utils.privat(s,username,"Серёга гей KappaPride")
            if message.strip() == "!suicide":
                utils.timeout(s,username,1)
                utils.mess(s,"@"+str(username)+" совершил суицид BloodTrail ")
            if message.strip() == "!cmd":
                utils.mess(s, "Мои команды: !mmr !game !time !update !strok !news !shutka !pogoda !piska_metr !mmr_metr !hromosom_metr !baltika_metr !youtube !suicide !ukraine !voteban")
                continue
            if message.strip() == "!mmr":
                if username == "thedukentre":
                    utils.mess(s,"@"+str(username)+" Папа, ты же уже знаешь как определять")
                    continue
                elif username == "serejaperviy":
                    utils.mess(s,"@"+str(username)+" Сам должен знать FailFish")
                    continue
                else:
                    utils.mess(s,"@"+str(username)+" Более точный ммр: "+str(mmr_set))
                    continue
            main = re.search(u"мейн", message)
            if len(str(main)) > 4:
                utils.mess(s, "!db")
                continue
            soob = re.search(u"вк",message)
            if len(str(soob))>5:
                utils.mess(s,"Вступай в группу: https://vk.com/serejaperviytv")
                continue
            soob = re.search(u"ютуб", message)
            if len(str(soob)) > 5:
                utils.mess(s, "Подписывайся на ютуб канал: https://www.youtube.com/channel/UCJqLjhNQtU4XBzrQXDtQj1g")
                continue
            soob = re.search(u"youtube", message)
            if len(str(soob)) > 5:
                utils.mess(s, "Подписывайся на ютуб канал: https://www.youtube.com/channel/UCJqLjhNQtU4XBzrQXDtQj1g")
                continue
            if message.strip() == "!youtube":
                utils.mess(s, "Подписывайся на ютуб канал: https://www.youtube.com/channel/UCJqLjhNQtU4XBzrQXDtQj1g")
                continue
            if message.strip() == "!ukraine":
                if ukraine_cooldawn == 0:
                    utils.mess(s,"SwiftRage SwiftRage СЛАВА УКРАИНЕ! SwiftRage SwiftRage")
                    ukraine_cooldawn = 20
                else:
                    utils.privat(s,username,"Кд "+str(ukraine_cooldawn)+" сек, и да, слава украине! BibleThump")
                continue
            if message.strip() == "!baltika_metr":
                if baltika_timer == 0:
                    baltika = random.randint(1,10)
                    if(baltika==1):
                        utils.mess(s,"@"+str(username)+" Сегодня я рекомендую тебе выпить балтику 0")
                    if (baltika == 2):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 2")
                    if (baltika == 3):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 3")
                    if (baltika == 4):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 4")
                    if (baltika == 5):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 5")
                    if (baltika == 6):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 6")
                    if (baltika == 7):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 7")
                    if (baltika == 8):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 8")
                    if (baltika == 9):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику 9")
                    if (baltika == 10):
                        utils.mess(s, "@" + str(username) + " Сегодня я рекомендую тебе выпить балтику Кулер")
                    baltika_timer = 5
                else:
                    utils.privat(s,username,"!baltika_metr перезаряжается "+str(baltika_timer)+" сек")
                continue
            soob = re.search(u"иди нахуй",message)
            if len(str(soob))>5:
                utils.mess(s,"@"+str(username)+" Сам иди DansGame")
                soob = "GG"
                continue
            if message.strip() == u"элеватор":
                utils.mess(s,"Я слышал, что звери, которых называют модераторами, могут забанить за это слово! Будь осторожней @" + str(username))
                continue
            if message.strip() == u"это элеватор":
                utils.mess(s,"Я слышал, что звери, которых называют модераторами, могут забанить за это слово! Будь осторожней @" + str(username))
                continue
            if message.strip() == u"это элеватор?":
                utils.mess(s,"Я слышал, что звери, которых называют модераторами, могут забанить за это слово! Будь осторожней @" + str(username))
                continue
            if message.strip() == u"привет бот":
                if username == "thedukentre":
                    utils.mess(s,"@"+str(username)+" Привет папа KonCha !")
                    continue
                elif username == "serejaperviy":
                    utils.mess(s,"@"+str(username)+" Привет паучок KonCha !")
                    continue
                elif utils.isOp(username):
                    utils.mess(s,"@"+str(username)+" Привет нечеловек KonCha !")
                    continue
                else:
                    utils.mess(s,"@"+str(username)+" Привет KonCha")
                    continue
            if message.strip() == u"бот привет":
                if username == "thedukentre":
                    utils.mess(s,"@"+str(username)+" Привет папа KonCha !")
                    continue
                elif username == "serejaperviy":
                    utils.mess(s,"@"+str(username)+" Привет паучок KonCha !")
                    continue
                elif utils.isOp(username):
                    utils.mess(s,"@"+str(username)+" Привет нечеловек KonCha !")
                    continue
                else:
                    utils.mess(s,"@"+str(username)+" Привет KonCha")
                    continue
            if message.strip() == u"бот":
                if username == "thedukentre":
                    utils.mess(s,"@"+str(username)+" Что папа CoolStoryBob ?")
                    continue
                elif username == "serejaperviy":
                    utils.mess(s,"@"+str(username)+" Что паучок CoolStoryBob ?")
                    continue
                elif utils.isOp(username):
                    utils.mess(s,"@"+str(username)+" Чего тебе?")
                    continue
                else:
                    utils.mess(s,"@"+str(username)+" Что случилось?")
                    continue
            if message.strip() == "!game":
                if game_timer == 0:
                    game = 1
                    utils.mess(s,"Игра началась! Загадываю слово")
                    random_word = random.randint(0,8)
                    sleep(2)
                    if(random_word == 0):
                        utils.mess(s,"Это имя нашего паучка")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s,"с _ _ _ _ _ 6 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s,"с _ _ _ _ _ 6 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s,"с _ _ _ _ а 6 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s,"с _ _ _ _ а 6 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s,"с _ р _ _ а 6 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s,"с _ р _ _ а 6 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s,"с _ р е _ а 6 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s,"с _ р е _ а 6 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s,"с _ р е ж а 6 букв")
                            if message.strip() == u"сережа":
                                winner = 1
                                utils.mess(s,"У нас есть победитель! Это - @"+str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if random_word == 1:
                        utils.mess(s, "название любимого героя стримера, на английском")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "b _ _ _ _ _ _ _ _ _ _ 11 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "b _ _ _ _ _ _ _ _ _ _ 11 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "b _ _ _ d _ _ _ _ _ _ 11 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "b _ _ _ d _ _ _ _ _ _ 11 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "b r _ _ d _ _ _ _ _ _ 11 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "b r _ _ d _ _ _ _ _ _ 11 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "b r _ _ d m o _ _ _ _ 11 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "b r _ _ d m o t _ _ _ 11 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "b r _ _ d m o t _ _ _ 11 букв")
                            if message.strip() == u"broodmother":
                                winner = 1
                                utils.mess(s,"У нас есть победитель! Это - @"+str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if (random_word == 2):
                        utils.mess(s, "Это ник моего создателя")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "t _ _ _ _ _ _ _ _ _ _ 11 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "t _ _ _ _ _ _ _ _ _ _ 11 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "t h e _ _ _ _ _ _ _ _ 11 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "t h e _ _ _ _ _ _ _ _ 11 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "t h e _ _ _ _ _ _ r e 11 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "t h e _ u _ _ _ _ r e 11 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "t h e _ u _ _ _ _ r e 11 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "t h e _ u k _ _ _ r e 11 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "t h e _ u k e _ _ r e 11 букв")
                            if message.strip() == u"thedukentre":
                                winner = 1
                                utils.mess(s,"У нас есть победитель! Это - @"+str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if (random_word == 3):
                        utils.mess(s, "Это ник моего главного врага")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "m _ _ _ _ _ 6 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "m _ _ _ _ _ 6 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "m _ _ b _ _ 6 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "m _ _ b _ _ 6 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "m o _ b _ _ 6 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "m o _ b _ _ 6 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "m o _ b _ t 6 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "m o _ b _ t 6 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "m o _ b _ t 6 букв")
                            if message.strip() == u"moobot":
                                winner = 1
                                utils.mess(s,"У нас есть победитель! Это - @"+str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if (random_word == 4):
                        utils.mess(s, "Это наши главные враги, именно они карают работяг!")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "м _ _ _ _ _ 6 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "м _ _ _ _ _ 6 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "м _ _ _ _ ы 6 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "м _ _ _ _ ы 6 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "м _ д _ _ ы 6 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "м _ д _ _ ы 6 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "м _ д е _ ы 6 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "м _ д е _ ы 6 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "м о д е _ ы 6 букв")
                            if message.strip() == u"модеры":
                                winner = 1
                                utils.mess(s,"У нас есть победитель! Это - @"+str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if (random_word == 5):
                        utils.mess(s, "Любимый напиток нашего алкаша стримера")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "б _ _ _ _ _ _ 7 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "б _ _ _ _ _ _ 7 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "б а _ _ _ _ _ 7 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "б а _ _ _ _ _ 7 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "б а _ т _ _ _ 7 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "б а _ т _ _ _ 7 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "б а _ т и _ _ 7 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "б а _ т и _ _ 7 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "б а _ т и _ а 7 букв")
                            if message.strip() == u"балтика":
                                winner = 1
                                utils.mess(s,"У нас есть победитель! Это - @"+str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if (random_word == 6):
                        utils.mess(s, "Лучшая страна в мире")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "у _ _ _ _ _ _ 7 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "у _ _ _ _ _ _ 7 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "у к _ _ _ _ _ 7 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "у к _ _ _ _ _ 7 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "у к _ _ и _ _ 7 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "у к _ _ и _ _ 7 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "у к _ _ и _ а 7 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "у к _ _ и _ а 7 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "у к _ а и _ а 7 букв")
                            if message.strip() == u"украина":
                                winner = 1
                                utils.mess(s, "У нас есть победитель! Это - @" + str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if (random_word == 7):
                        utils.mess(s, "Бомбят .....")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "д _ _ _ _ _ _ 7 букв")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "д _ _ _ _ _ _ 7 букв")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "д _ н _ _ _ _ 7 букв")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "д _ н _ _ _ _ 7 букв")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "д _ н _ _ с _ 7 букв")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "д _ н _ _ с _ 7 букв")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "д _ н б _ с _ 7 букв")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "д _ н б _ с _ 7 букв")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "д _ н б _ с с 7 букв")
                            if message.strip() == u"донбасс":
                                winner = 1
                                utils.mess(s, "У нас есть победитель! Это - @" + str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    if (random_word == 8):
                        utils.mess(s, "Имя дяди паука из лунтика")
                        sleep(2)
                        sek = 0
                        while winner == 0:
                            response = s.recv(1024).decode("utf-8")
                            username = re.search(r"\w+", response).group(0)
                            message = chat_message.sub("", response)
                            print(response)

                            if popitka == 0 and sek == 0:
                                utils.mess(s, "ш _ _ _  4 буквы")
                            if popitka == 1 and sek == 0:
                                utils.mess(s, "ш _ _ _  4 буквы")
                            if popitka == 2 and sek == 0:
                                utils.mess(s, "ш _ _ _  4 буквы")
                            if popitka == 3 and sek == 0:
                                utils.mess(s, "ш _ _ _  4 буквы")
                            if popitka == 4 and sek == 0:
                                utils.mess(s, "ш _ ю _  4 буквы")
                            if popitka == 5 and sek == 0:
                                utils.mess(s, "ш _ ю _  4 буквы")
                            if popitka == 6 and sek == 0:
                                utils.mess(s, "ш _ ю _  4 буквы")
                            if popitka == 7 and sek == 0:
                                utils.mess(s, "ш _ ю _  4 буквы")
                            if popitka > 7 and sek == 0:
                                utils.mess(s, "ш _ ю к  4 буквы")
                            if message.strip() == u"шнюк":
                                winner = 1
                                utils.mess(s, "У нас есть победитель! Это - @" + str(username))
                            sek = sek + 1
                            if sek == 6:
                                popitka = popitka + 1
                                sek = 0
                            print(sek)
                            print(popitka)
                            sleep(1)
                    game_timer = 30
                else:
                    utils.mess(s,"@"+str(username)+" До игры осталось "+str(game_timer)+" секунд")
                winner = 0
                game = 0

            if message.strip() == "!update":
                utils.mess(s,"Новости последних обновлений: версия 1 8 2 : Добавлена команда !voteban SwiftRage SwiftRage")
                continue
            if message.strip() == "!strok":
                strok = 9 + 21 + 951
                utils.mess(s,"Строк кода на данный момент: "+str(strok))
                continue
            if message.strip() == "!news":
                random_news = random.randint(0,3)
                if random_news == 0:
                    utils.mess(s,"Россия 24: на украине из-за нищеты начали питаться младенцами, сообщает корреспондент россии 24")
                elif random_news == 1:
                    utils.mess(s,"Рен-тв: Недавно нашей редакцией был замечен настоящий человек паук, только он выглядит не так, как мы его представляли...")
                elif random_news == 2:
                    utils.mess(s,"1 Канал: Украинский миллиардер под именем Сергей зарабатывает миллионы на своих зрителях")
                elif random_news == 3:
                    utils.mess(s,"Ns выпустил новые фишки на менёра, рекомендую не заходить в доту пару деньков")
            if message.strip() == "!shutka":
                random_shutka = random.randint(0,8)
                if random_shutka == 0:
                    utils.mess(s,"То что никто не может найти украинских монет 19 века, доказывает, что уже тогда украинцы использовали банковские карты.")
                if random_shutka == 1:
                    utils.mess(s,"Говорят, что все стримеры геи... Я тоже в это верю")
                if random_shutka == 2:
                    utils.mess(s,"Чтобы гей-парад в Киеве прошел успешно, туда надо пригласить @serejaperviy.")
                if random_shutka == 3:
                    utils.mess(s,"Пошел житель ДНР на озеро, закинул удочку и поймал большого карпа. Приносит домой, дает жене и говорит: Давай, жена, приготовь нам рыбки.Жена в ответ: Да где ж я тебе возьму воды, чтобы его почистить и помыть, да и газа нет, чтобы приготовить, даже электричества нет, чтобы просто свет зажечь.Карп поднимает голову и говорит: Слава Украине!")
                if random_shutka == 4:
                    utils.mess(s,"Люди, я открою вам большую тайну....... Ваш стример KappaPride ")
                if random_shutka == 5:
                    utils.mess(s,"Пришел мужик к священнику и говорит: Я грех совершил. Обманул еврея...Батюшка отвечает: Это — не грех. Это — чудо!")
                if random_shutka == 6:
                    utils.mess(s,"Идёт драка... Снайпер убивает медведя лд. После драки в чате: ЛД: снайп сколько голды получил за медведя? Снайп: 300 ЛД: ОТСОСИ У ТРАКТОРИСТА!!")
                if random_shutka == 7:
                    utils.mess(s,"Висп повесился")
                if random_shutka == 8:
                    utils.mess(s,"Я помню чудное мгновенье. Передо мной явилась ты. Потом криты по 1300. Мой труп в лесу нашли крипы.")
            if message.strip() == "MrDestructoid":
                utils.mess(s,"MrDestructoid MrDestructoid MrDestructoid")
                continue
            if message.strip() == u"бб":
                utils.mess(s,"пока!")
                continue
            music = re.search(u"какая музыка", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"что за музыка", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
            music = re.search(u"название музыки", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"название песни", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"что за песня", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"какая музыка?", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"что за музыка?", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"название музыки?", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"название песни?", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            music = re.search(u"что за песня?", message)
            if len(str(music)) > 5:
                utils.mess(s, "@" + str(username) + " Можно увидеть в левом верхнем углу")
                music = "GG"
                continue
            mmr = re.search(u"сколько рейта", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"сколько рейт", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"сколько ммр", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"какой рейт", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"какой это рейт", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"какой ммр", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"сколько рейта?", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"сколько рейт?", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"сколько ммр?", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"какой рейт?", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"какой это рейт?", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            mmr = re.search(u"какой ммр?", message)
            if len(str(mmr)) > 5:
                utils.mess(s, "@" + str(username) + " Более точный ммр: "+str(mmr_set))
                mmr = "GG"
                continue
            y4ilsa = re.search(u"учился", message)
            if len(str(y4ilsa)) > 5:
                utils.mess(s, "@" + str(username) + " У Серёжи 10 тысяч игр на бруде")
                y4ilsa = "GG"
                continue
            soob = re.match(r"!pogoda",message)
            print (message)

            if len(str(soob))>6:
                if pogoda_timer == 0:
                    city = re.findall(r"\w*",message)
                    print city[3]
                    print soob.group(0)
                    if len(str(city[3])) > 3:
                        response = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?q=" + str(city[3]) + ",{country code}&cnt=1" + "&appid=092256fd49a7f092ad96139ce8f9e62a")
                        j = response.json()
                        udayn = j["list"][0]["dt"]
                        date = datetime.datetime.fromtimestamp(int(udayn)).strftime("%d-%m-%Y")
                        eve_temp = j["list"][0]["temp"]["eve"]
                        eve_temp = eve_temp - 273
                        description = j["list"][0]["weather"][0]["description"]
                        utils.mess(s,"@"+str(username)+" Время: "+str(date)+" Город: "+str(city[3])+" Температура сегодня: "+ str(eve_temp)+" Описание: "+ str(description))
                        pogoda_timer = 6
                    else:
                        utils.mess(s,"Чтобы узнать погоду введите: !pogoda [City] ,город(City) вводите на английском")
                    soob = "GG"
                else:
                    utils.privat(s,username,"!pogoda перезаряжается "+str(pogoda_timer)+" сек")
                continue
            soob = re.search(u"слава украине",message)
            if len(str(soob)) > 5:
                utils.mess(s,"@"+str(username)+" Героям слава!")
                continue
            soob = re.search(u"люкан", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Howl!")
                continue
            soob = re.search(u"энигма", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Энигма, жизнь моих деток куда ценнее твоих!")
                continue
            soob = re.search(u"шейкер", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Шейкер, без тебя жизнь моих деток станет куда легче!")
                continue
            soob = re.search(u"бруда", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Лапки становятся сильней!")
                continue
            if message.strip() == "!piska_metr":
                if piska_timer == 0:
                    if username == "thedukentre":
                        piska = 23
                        utils.mess(s,"@" + str(username) + " Ваш писюн равен "+str(piska)+" см! WutFace WutFace ")
                    elif username == "serejaperviy":
                        piska = random.randint(1,5)
                        utils.mess(s, "@" + str(username) + " Ваш писюн равен " + str(piska) + " см! MingLee MingLee ")
                    else:
                        piska = random.randint(1, 23)
                        utils.mess(s, "@" + str(username) + " Ваш писюн равен " + str(piska) + " см! TehePelo TehePelo ")
                    piska_timer = 4
                else:
                    utils.privat(s,username,"!piska_metr перезаряжается "+str(username)+" сек")
                continue
            if message.strip() == "!mmr_metr":
                if mmr_timer == 0:
                    if username == "thedukentre":
                        random_mmr = random.randint(9000,9800)
                        utils.mess(s,"@" + str(username) + " Ваш ммр равен "+str(random_mmr)+" WutFace WutFace ")
                    elif username == "serejaperviy":
                        random_mmr = random.randint(1,2500)
                        utils.mess(s, "@" + str(username) + " Ваш ммр равен " + str(random_mmr) + " UnSane UnSane  ")
                    else:
                        random_mmr = random.randint(1, 9800)
                        utils.mess(s, "@" + str(username) + " Ваш ммр равен " + str(random_mmr) + " DendiFace DendiFace")
                    mmr_timer = 4
                else:
                    utils.privat(s,username,"!mmr_metr перезаряжается "+str(mmr_timer)+" сек")
                continue
            if message.strip() == "!hromosom_metr":
                hromosom = random.randint(44,49)
                utils.mess(s,"@"+str(username)+" У вас "+str(hromosom)+" хромосом SeemsGood")
                continue
            soob = re.search(u"мубот пидр",message)
            if len(str(soob))>5:
                utils.mess(s,"@"+str(username)+" Конечно")
                continue
            soob = re.search(u"привет",message)
            if len(str(soob))>5:
                utils.mess(s,"@"+str(username)+" Привет KonCha")
                continue
            soob = re.search(u"хай", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Привет KonCha")
                continue
            soob = re.search(u"здарово", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Привет KonCha")
                continue
            soob = re.search(u"@SerejaBot", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Я ещё глуп, чтобы тебе нормально ответить")
                continue
            soob = re.search(u"пиздец|сука|блядь|блять|нахуй|пидор|пидр", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " Не ругайся пожалуйста BibleThump ")
                soob = "GG"
                continue
            soob = re.search(u"наебал", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " СТРИМЕР НАЕБАЛ SwiftRage  ")
                soob = "GG"
                continue
            soob = re.search(u"наёбщик", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " СТРИМЕР НАЕБАЛ SwiftRage  ")
                soob = "GG"
                continue
            soob = re.search(u"наёбсик", message)
            if len(str(soob)) > 5:
                utils.mess(s, "@" + str(username) + " СТРИМЕР НАЕБАЛ SwiftRage  ")
                soob = "GG"
                continue
            if timebot == 5:
                randomtime = random.randint(0,6)
                if randomtime == 0:
                    utils.mess(s,"Мои умения можно посмотреть командой !cmd")
                elif randomtime == 1:
                    utils.mess(s,"Вы можете предложить улучшение для бота: !ho4y [улучшение]. Ваше сообщение будет записано и передано разработчику")
                elif randomtime == 2:
                    utils.mess(s,"Хочешь произвести впечатление на девушек, тогда введи !piska_metr")
                elif randomtime == 3:
                    utils.mess(s,"Хочешь похвастаться перед друзьями ммр? Тогда введи !mmr_metr")
                elif randomtime == 4:
                    utils.mess(s,"Считаешь себя отсталым или сверхчеловеком? Тогда введи !hromosom_metr")
                elif randomtime == 5:
                    utils.mess(s,"Хочешь узнать погоду в своём городе? Тогда введи: !pogoda [City] ,город нужно вводить на английском!")
                elif randomtime == 6:
                    utils.mess(s,"Новости последних обновлений: версия 1 8 2 : Добавлена команда !voteban SwiftRage SwiftRage")
        sleep(0.5)





if __name__ == "__main__":
    main()