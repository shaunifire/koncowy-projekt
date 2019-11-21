from django.shortcuts import render
#from .models import Odpowiedz
import random



    #chosen == 99 to zmienna kontrolna, która zmieni się gdy zostanie wysłana informacja z templatki z kliknięciem na button. Ponieważ będzie ona miała wartość zgodną z randomową liczbą wybraną prze kompa, muszę jej nadać kontrolną liczbę która NA PEWNO nie wystąpi podczaslosowania.
def funkcja_buttona(request):
    chosen=99
    if request.method=='POST':
        chosen=request.POST.get("wybor")
    return test(request,chosen)
    #ładujemy bazę danych

def test (request, chosen=99):
    import os
    import pandas
    import csv
    lista=[]
    with open('ChatBotApp/pyt.csv', 'r', newline='\n') as csvfile:
        data=csv.reader(csvfile)
        dictionary=[]
        for row in data:
            for i in row:
                dictionary.append(i.split(',')[0])
    #Ładujemy pytania do bota które wrzucimy pod listę radio. Zrobiłam to bez pętli, żeby moja partnerka rozumiała co się dzieje.
    pytanie1=random.randint (0,len(dictionary)-1)
    pytanie2=random.randint (0,len(dictionary)-1)
    pytanie3=random.randint (0,len(dictionary)-1)
    pytanie4=random.randint (0,len(dictionary)-1)
    button1=dictionary[pytanie1][0]
    button2=dictionary[pytanie2][0]
    button3=dictionary[pytanie3][0]
    button4=dictionary[pytanie4][0]
    #testowa=pytanie1
        #zmienna chosen jest wysyłana do nas za drugim załadowaniem, więc zmienia wartość z 99 na 1-4
    if chosen!=99:
        odpowiedz=random.randint(1,dictionary[chosen])
        odpowiedz_bota_z_listy=dictionary[chosen][odpowiedz]
        return render (request, 'odpowiedz.html', {"button1":button1,"button2":button2,"button3":button3,"button4":button4, "odpowiedz_bota_z_listy":odpowiedz_bota_z_listy} )
    else:
        return render (request, 'odpowiedz.html', {"button1":button1,"button2":button2,"button3":button3,"button4":button4, "odpowiedz_bota_z_listy":"ddddddddddkdkdkdkdkd"} )
