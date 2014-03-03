import os
import sys
import math
import string
import random
def my_view(request):
   	return {'project':'zodiac'}
def home_view(request):
	if request.method=="POST":
		dia=request.POST["dia"]
		mes=request.POST["mes"]
		dia=int(dia)
		mes=int(mes)
		frase=["Tindras una bona setmana","Tindras una mala setmana","Tindras un bon mes","Tindras un mal mes","Preparat per que moriras entre 0 i 90 anys"]
		aleatori=random.randint(0, 4)
		if (dia>=21 and mes==3) or (dia<=20 and mes==4):
			signo = "Aries"
			img = "../static/aries.png"
		elif (dia>=21 and mes==4) or (dia<=21 and mes==5):
			signo="Tauro"
			img = "../static/tauro.png"
		elif (dia>=22 and mes==5) or (dia<=21 and mes==6):
			signo= "Geminis"
			img = "../static/gemini.png"
		elif (dia>=22 and mes==6) or (dia<=22 and mes==7):
			signo = "Cancer"
			img = "../static/cancer.png"
		elif (dia>=23 and mes==7) or (dia<=22 and mes==8):
			signo="Leo"
			img = "../static/leo.png"
		elif (dia>=23 and mes==8) or (dia<=22 and mes==9):
			signo = "Virgo"
			img = "../static/virgo.png"
		elif (dia>=23 and mes==9) or (dia<=22 and mes==10):
			signo = "Libra"
			img = "../static/libra.png"
		elif (dia>=23 and mes==10) or (dia<=22 and mes==11):
			signo="Escorpio"
			img= "../static/escorpio.png"
		elif (dia>=23 and mes==11) or (dia<=21 and mes==12):
			signo = "Sagitario"
			img= "../static/sagitario.png"
		elif (dia>=22 and mes==12) or (dia<=20 and mes==1):
			signo="Capricornio"
			img="../static/capricornio.png"
		elif (dia>=21 and mes==1) or (dia<=19 and mes==2):
		    	signo = "Aquario"
			img="../static/aquario.png"
		elif (dia>=20 and mes==2) or (dia<=20 and mes==3):
			signo= "Piscis"
			img= "../static/piscis.png"
		return{'project':'zodiac','signo':signo,'imagen':img,'frase':frase[aleatori]}
	return{'project':'zodiac','signo':'',}


