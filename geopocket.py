#! /usr/bin/env python
# -*- coding: utf-8 -*-

import about
import math
import matplotlib.pyplot as plt

# %% ABOUT GEOPOCKET

about.about
about.navodila

# %% 00. Pretvorbe kotov

def dms2rad(dms:float):
    """Funkcija pretvori kot iz decimalnih vrednosti v radiane.
    
    :param dms: Kot v decimalnih stopnijah
    :return: Kot v radianih"""
    
    rad = math.radians(dms)
    return rad

def rad2dms(rad:float):
    """Funkcija pretvori kot iz radianov v decimalne vrednosti kotov.
    
    :param rad: Kot v radianih
    :return: Kot v stopinjah"""
    
    dms = math.degrees(rad)
    return dms

# %% 01. Dolžina

def dol(y1:float,x1:float,y2:float,x2:float): #iz kooridnat
    """Funkcija izračuna horizontalno dolžino med dvema točkama. 
     
    T1(y1,x1) - prva točka
    T2(y2,x2) - druga točka
    
    :param y1: Y koordinata prve točke
    :param x1: X koordinata prve točke
    :param y2: Y koordinata druge točke
    :param x2: X koordinata druge točke
    
    :return: Razdalja med točkama
    
    :Example:
    >>> 
    >>> y1 = 505
    >>> x1 = 120
    >>> y1 = 735
    >>> x1 = 90
    >>> dol(y1,x1,y2,x2)
    """
    
    
    

    dolzina = math.sqrt((y2-y1)**2 + (x2-x1)**2)
    return dolzina

# %% 02. Smerni kot

def ni(y1:float, x1:float, y2:float, x2:float):
    """Funkcija računa poljubni smerni kot med dvema točkama, rezultat vrne v radianih.
    Za pretvorbo radianov v decimalne vrednosti uporabi funkcijo nidms(ni(y1,x1,y2,x2))
    
    :param y1: Y koordinata prve točke
    :param x1: X koordinata prve točke
    :param y2: Y koordinata druge točke
    :param x2: X koordinata druge točke
    
    :return: Funkcija vrne rezultat v radianih, za pretvorbo v decimalne vrednosti kliči nidms(ni(y1,x1,y2,x2))
    
    :Example:
    >>> 
    >>> y1 = 451123.443
    >>> x1 = 100235.123
    >>> y1 = 451860.231
    >>> x1 = 98213.456
    >>> smerni_kot = nidms(ni(y1,x1,y2,x2))"""

    #FUNKCIJA
    delY = y2-y1
    delX = x2-x1
    

    if (delY > 0) and (delX > 0): #1. kvadrant
        ni = math.atan(((delY/delX)))
    elif (delY > 0) and (delX < 0): #2. kvadrant
        ni = math.atan(((delY/delX))) + math.pi
    elif (delY < 0) and (delX < 0): #3. kvadrant
        ni = math.atan(((delY/delX))) + math.pi
    elif (delY < 0) and (delX > 0): #4. kvadrant
        ni = math.atan(((delY/delX))) + 2*math.pi
    elif delY == 0 and delX < 0:
        ni = math.pi
    elif delY > 0 and delX == 0:
        ni = math.pi/2
    elif delY < 0 and delX == 0:
        ni = (3/2)*math.pi
    elif delY == 0:
        ni = print("Smerni kot ne obstaja!!!")
    elif delX == 0:
        ni == 0

    #nist = nidms(ni)
    #print("ni[dms] = {:3.4f}".format(nist))
    #print()
	
    return ni

def nidms(ni):
    """Funkcija pretvori smerni kot iz radianov v decimalne kotne vrednosti.
    
    :param ni: smerni kot v radianih"""
    
    nidms = math.degrees(ni)
    return nidms

# %% 1. FreeStation - prosto stojišče z dvema navezovalnima točkama
#prosto_info = webbrowser.open("https://repozitorij.uni-lj.si/Dokument.php?id=85900&lang=slv")

def prosto(yA:float,xA:float,yB:float,xB:float,rA_dms:float,rB_dms:float,dolA:float,dolB:float):

    #Sphinx
    """Funkcija izračuna koordinate prosto izbranega stojišča z dvema navezovalnima točkama
       Postopek izračuna je opisan: https://repozitorij.uni-lj.si/Dokument.php?id=85900&lang=slv
       
    :param yA: Y koordinata prve navezovalne točke
    :param xA: X koordinata prve navezovalne točke
    :param yB: Y koordinata druge navezovalne točke
    :param xB: X koordinata druge navezovalne točke
    :param rA_dms: Polarna meritev kota do navezovalne točke A [dms]
    :param rB_dms: Polarna meritev kota do navezovalne točke B [dms]
    :param dolA: Merjena dolžina do prve navezovalne točke A
    :param dolA: Merjena dolžina do prve navezovalne točke B
    :return: Funkcija vrne izračunane koordinate prostega stojišča, grafično izriše geometrijo točk in izračunane vrednosti izpiše na *.txt in *csv.
    
    :Example:
    >>> 
    >>> yA = 461832.5000
    >>> xA = 99989.5800 
    >>> yB = 459937.1900
    >>> xB = 101345.0000
    >>> rA_dms = 65.1230
    >>> rB_dms = 120.4558
    >>> dolA = 625.12
    >>> dolB = 715.09
    >>> prosto(yA,xA,yB,xB,rA_dms,rB_dms,dolA,dolB))"""
    
    if ((yA or xA) or (yB or xB) or (rA_dms or rB_dms) or (dolA or dolB)) > 0.0:
        print("Računam...")
        print()
        #Pretvorba kotov v radiane
        rA = dms2rad(rA_dms)
        rB= dms2rad(rB_dms)
        #Smerni kot med navezovalnima točkama
        niAB = ni(yA,xA,yB,xB)
        #Kot gama
        gama = rA-rB
        if gama < 0.0:   #Negativnih kotov v naravi ni!
            gama = gama + 2*math.pi
            #print(gama)
        else:
            gama = gama
        #print(rad2dms(gama))
        dr = math.sqrt((dolA**2)+(dolB**2)-(2*dolA*dolB*math.cos(gama))) #meritve, ne koordinate
        dAB = dol(yA,xA,yB,xB) #koordinate, ne meritve
        #Izravnava izmerjenih dolžin - dA in dB glede na merilo mreže s faktorjem merila m
        m = dAB/dr
        dA = m*dolA
        dB = m*dolB
        #Izračun kota alfa
        alfa = math.tan((2*dA*dB*math.sin(gama))/((dr**2) + dA**2 - dB**2))
        #Koordinate prostega stojišča
        sps = niAB + alfa
        if sps < 0:
            sps = sps + 2*math.pi
        elif sps > (2*math.pi):
            sps = sps - 2*math.pi
        else:
            sps = sps
        
        xps = xA+m*dA*(math.cos(sps))
        yps = yA+m*dA*(math.cos(sps))
        
        #Če zaradi geometrije pride do negativnih vrednosti koordinat, potem spremeni vrednost koordinat na pozitivno!
        
        Xps = abs(xps)
        Yps = abs(yps)
        
        #GRAFIČNA PREDSTAVITEV - matplotlib
        
        x = [xA,xB,Xps]
        y = [yA,yB,Yps]
        n1 = [xA,Xps]
        n2 = [yA,Yps]
        
        plt.title("Prosto stojišče: Geometrija")
        plt.grid()
        plt.autoscale(enable = True, axis = 'both')
        plt.ylabel("X [m]")
        plt.xlabel("Y [m]")
        plt.scatter(y,x,marker = 'o', color = 'b') 
        plt.plot(y,x, 'b')
        plt.plot(n2,n1, 'b')
        plt.plot(Yps,Xps, 'r')
        plt.text(yA,xA, "A",color = 'k',style = 'normal',fontsize = 11)
        plt.text(yB,xB,"B",color = 'k',style = 'normal',fontsize = 11)
        plt.text(Yps,Xps,"ST",color = 'k',style = 'italic',fontsize = 11)
        plt.show()
        
        print("Rezultati: ")
        print(" Y = {:.4f}".format(Yps))
        print(" X = {:.4f}".format(Xps))
        print()
        
        # IZPIS REZULTATOV - txt
        prosto_txt = open("rezultati.txt", "a")
                
        prosto_txt.write("Prosto_stojisce\n")
        prosto_txt.write("------------------------------------\n")
        prosto_txt.write("Vhodni podatki:\n")
        prosto_txt.write("yA = {:.4f} \n".format(yA))
        prosto_txt.write("xA = {:.4f} \n".format(xA))
        prosto_txt.write("yB = {:.4f} \n".format(yB))
        prosto_txt.write("xB = {:.4f} \n".format(xB))
        prosto_txt.write("polarni kot A =  {:3.4f} \n".format(rA_dms))
        prosto_txt.write("polarni kot B =  {:3.4f} \n".format(rB_dms))
        prosto_txt.write("razdalja A =  {:.4f} \n".format(dolA))
        prosto_txt.write("razdalja B =  {:.4f} \n".format(dolB))
        prosto_txt.write("------------------------------------\n")
        prosto_txt.write("Koordinate nove tocke: \n")
        prosto_txt.write("Y: {:.4f} \n".format(Yps))
        prosto_txt.write("X: {:.4f} \n".format(Xps))
        prosto_txt.write("------------------------------------\n")
        
        prosto_txt.close()
        
        #IZPIS REZULTATOV - csv
        prosto_csv = open("izracuni.csv", "a")
        
        prosto_csv.write("Prosto_stojisce,yA,xA,yB,xB,rA_dms,rB_dms,dolA,dolB,Yps,Xps\n") #header
        
        dec = "{:.4f},"
        dec_last = "{:.4f}\n"

        prosto_csv.write("Vrednosti,")
        prosto_csv.write(dec.format(yA))
        prosto_csv.write(dec.format(xA))
        prosto_csv.write(dec.format(yB))
        prosto_csv.write(dec.format(xB))
        prosto_csv.write(dec.format(rA_dms))
        prosto_csv.write(dec.format(rB_dms))
        prosto_csv.write(dec.format(dolA))
        prosto_csv.write(dec.format(dolB))
        prosto_csv.write(dec.format(Yps))
        prosto_csv.write(dec_last.format(Xps))
        
        prosto_csv.close()

    elif ((yA or xA) or (yB or xB) or (rA_dms or rB_dms) or (dolA or dolB)) < 0.0:
        print("Negativnih koordinat, dolžin ali smeri ne sprejemam!")
    else:
        print("Ker pač mora bit.")
        return
    
# %% 2. Zunanji urez

def zunanji(yA:float,xA:float,yB:float,xB:float,zsA:float,zsB:float):
    
    #Sphinx
    """Zunanji urez je postopek določitve koordinat neznane točke na osnovi opazovanih zunanjih smeri iz dveh danih točk.
    Zunanja smer je smer iz dane točke na novo točko.
    Orientirana smer je kot, ki ga oklepa neka smer s severom.
       
    :param yA: Y koordinata točke
    :param xA: X koordinata točke
    :param yB: Y koordinata druge točke
    :param xB: X koordinata druge točke
    :param zsA: Zunanja smer iz točke A na novo točko [dms]
    :param zsB: Zunanja smer iz točke B na novo točko [dms]
    
    :return: Funkcija vrne koordinate nove točke, grafično izriše geometrijo točk in izračunane vrednosti izpiše na *.txt in *csv.
    
    :Example:
    >>>
    >>> yA = 461832.50 
    >>> xA = 99989.58
    >>> yB = 459937.19
    >>> xB = 101340.75
    >>> zsA = 65.2433
    >>> zsB = 75.1345
    >>> zunanji(yA,xA,yB,xB,zsA,zsB)
    """

    if ((yA or xA) or (yB or xB) and (zsA or zsB)) > 0.0:
        #smerni koti, dolžine
        niABz = ni(yA,xA,yB,xB)
        niBAz = ni(yB,xB,yA,xA)
        dz = dol(yA,xA,yB,xB)
        #orientirane smeri
        fiA = niABz+dms2rad(zsA)
        fiB = niBAz-dms2rad(zsB)
        
        if (fiA or fiB) > 0.0: #problem negativnih kotov
            fiA = fiA + 2*math.pi
            fiB = fiB + 2*math.pi
        else:
            fiA = fiA
            fiB = fiB
        #Kot delta
        deltaaA = fiA - niABz
        deltaaB = niBAz - fiB
        deltaa = fiB-fiA
        
        if (deltaaA or deltaaB or deltaa) < 0.0: #problem negativnih kotov
            deltaaA = deltaaA + 2*math.pi
            deltaaB = deltaaB + 2*math.pi
            deltaa = deltaa + 2*math.pi
        else:
            deltaaA = deltaaA
            deltaaB = deltaaB
            deltaa = deltaa
        #kontrola
        del_all = rad2dms(abs(deltaaA+deltaaB+deltaa))
        k = 180.0
        #Izračun stranic trikotnika iz sinusnega izreka
        bz = (dz/math.sin(deltaa))*math.sin(deltaaA)
        az = (dz/math.sin(deltaa))*math.sin(deltaaB)
        #Izračun koordinatnih razlik
        delyA = az*math.sin(fiA)
        delxA = az*math.cos(fiA)
        delyB = bz*math.sin(fiB)
        delxB = bz*math.cos(fiB)
        #Koordinate nove točke
        yZa = yA + delyA
        xZa = xA + delxA
        yZb = yB + delyB
        xZb = xB + delxB
        #Kontrola
        if (del_all == k):
            print("Koordinati sta enaki iz obeh smeri! \t Razlika = {:.4f}".format(abs((yZb-yZa)+(xZa-xZb))))
             
            #Končna vrednost
            yZ = abs(yZa)
            xZ = abs(xZa)
            
            #GRAFIČNA PREDSTAVITEV - matplotlib
            
            x1 = [xA,xB,xZ]
            y1 = [yA,yB,yZ]
            m1 = [xA,xZ]
            m2 = [yA,yZ]
            
            plt.title("Zunanji urez: Geometrija")
            plt.grid(True)
            plt.autoscale(enable = True, axis = 'both')
            plt.ylabel("X [m]")
            plt.xlabel("Y [m]")
            plt.scatter(y1,x1,marker = 'o', color = 'r') 
            plt.plot(y1,x1, "b")
            plt.plot(m2,m1, "b")
            plt.text(yA,xA, "A",color = 'k',style = 'normal', fontsize = 11)
            plt.text(yB,xB,"B",color = 'k',style = 'normal', fontsize = 11)
            plt.text(yZ,xZ,"Z",color = 'k',style = 'normal',fontsize = 11)
            plt.show()
            
            #Rezultati
            print("Rezultati: ")
            print(" Y = {:.4f}".format(yZ))
            print(" X = {:.4f}".format(xZ))
            print()
            
            #yK = round(yZ,4)
            #xK = round(xZ,4)
            
            #IZPIS na txt
            zun_rez = open("rezultati.txt", "a")
                
            zun_rez.write("Zunanji urez\n")
            zun_rez.write("------------------------------------\n")
            zun_rez.write("Vhodni podatki:\n")
            zun_rez.write("yA = {:.4f} \n".format(yA))
            zun_rez.write("xA = {:.4f} \n".format(xA))
            zun_rez.write("yB = {:.4f} \n".format(yB))
            zun_rez.write("xB = {:.4f} \n".format(xB))
            zun_rez.write("zunanja smer A =  {:3.4f} \n".format(zsA))
            zun_rez.write("zunanja smer B =  {:3.4f} \n".format(zsB))
            zun_rez.write("------------------------------------\n")
            zun_rez.write("Koordinate nove tocke: \n")
            zun_rez.write("Y: {:.4f} \n".format(yZ))
            zun_rez.write("X: {:.4f} \n".format(xZ))
            zun_rez.write("------------------------------------\n")
            zun_rez.close()
            
             #IZPIS REZULTATOV - csv
            zun_csv = open("izracuni.csv", "a")
            zun_csv.write("Zunanji_urez,yA,xA,yB,xB,zsA,zsB,yZ,xZ\n") #header
        
            dec = "{:.4f}," #prvi in ostali
            dec_last = "{:.4f}\n" #zadnji

            zun_csv.write("Vrednosti,")
            zun_csv.write(dec.format(yA))
            zun_csv.write(dec.format(xA))
            zun_csv.write(dec.format(yB))
            zun_csv.write(dec.format(xB))
            zun_csv.write(dec.format(zsA))
            zun_csv.write(dec_last.format(zsB))
        
            zun_csv.close()
         
    elif ((yA or xA) and (yB or xB) and (zsA or zsB)) < 0.0:
        print("Negativne koordinate in zunanje smeri ne sprejemam...")
    else:
        print("---")
    return

# %% 3. Notranji urez

def notranji(yA:float,xA:float,yB:float,xB:float,yC:float,xC:float,alfa:float,beta:float):
    
    #Sphinx
    """Notranji urez je postopek določitve koordinat neznane točke na osnovi opazovanih smeri iz nove točke do danih točk.
       Notranja smer je smer iz nove točke na dano točko.
       Postopek lahko rešimo na več načinov, pri izračunu smo uporabili Snelliusov način.

    :param yA: Y koordinata prve točke
    :param xA: X koordinata prve točke
    :param yB: Y koordinata druge točke
    :param xB: X koordinata druge točke
    :param yC: Y koordinata tretje točke
    :param xC: X koordinata tretje točke
    :param alfa: Notranja smer iz nove točke N na točko A [dms]
    :param beta: Notranja smer iz nove točke N na točko B [dms]
    
    :return: Funkcija vrne koordinate nove točke, grafično izriše geometrijo točk in izračunane vrednosti izpiše na *.txt in *csv.
    
    :Example:
    >>> 
    >>> yA = 461832.50 
    >>> xA = 99989.58
    >>> yB = 459937.19
    >>> xB = 101340.75
    >>> yC = 461958.90
    >>> xC = 101121.14
    >>> alfa = 75.1765
    >>> beta = 45.4318
    >>> notranji(yA,xA,yB,xB,yC,xC,alfa,beta)
    """
    
    if ((yA or xA) and (yB or xB) and (yC or xC) and (alfa or beta)) > 0.0:
        print("Računam...")
        #0. dms2rad
        alfa = dms2rad(alfa)
        beta = dms2rad(beta)
        
        #Notranji urez - Snellius
        #smerni koti, dolžine
        niAB = ni(yA,xA,yB,xB)
        niBA = ni(yB,xB,yA,xA)
        niBC = ni(yB,xB,yC,xC)
        dAB = dol(yA,xA,yB,xB) #a
        dBC = dol(yB,xB,yC,xC) #b
        #(fi+psi)/2 = C
        c = math.pi - ((alfa + beta + niBA - niBC)/2)
        # kot Mi
        mi = math.atan((dAB*math.sin(beta))/(dBC*math.sin(alfa)))
        # (fi-psi)/2 = D
        d = math.atan(math.tan(c)/math.tan((math.pi/4)+mi))
        # kot Fi
        fi = c+d
        # kot Psi
        psi = c-d
        #Dolžine stranic
        dAN = (dAB/math.sin(alfa))*math.sin(alfa+fi)
        dCN = (dBC/math.sin(beta))*math.sin(beta+psi)
        #Smerna kota do nove točke
        niAN = niAB + fi
        niCN = niBC + (math.pi-psi)
        
        #Izračun koordinatnih razlik
        delyN1 = dAN*math.sin(niAN) #A
        delxN1 = dAN*math.cos(niAN) #A
        delyN2 = dCN*math.sin(niCN) #C
        delxN2 = dCN*math.cos(niCN) #C
        
        #Koordinate nove točke; pogoj: N1 = N2 --> N1 = N2 = N
        # 1. 
        yN1 = yA + delyN1
        xN1 = xA + delxN1
        
        # 2. 
        yN2 = yC + delyN2
        xN2 = xC + delxN2
        
        #zaokrožitev zaradi enakosti koordinat iz obeh strani
        #če je geometrija točk slaba pride do odstopanja na 12. decimalki
        yN1r = round(yN1,8)
        xN1r = round(xN1,8)
        yN2r = round(yN2,8)
        xN2r = round(xN2,8)
        
        #kontrola enakosti N1 in N2
        if (yN1r == yN2r) and (xN1r == xN2r):
            print()
            print("Koordinati sta enaki iz obeh smeri, bravo!")
            
            yN = yN1r
            xN = xN2r
            
            #GRAFIČNA PREDSTAVITEV - matplotlib
            
            x1 = [xA,xB,xC,xN]
            y1 = [yA,yB,yC,yN]
            
            ny = [yN]
            nx = [xN]
            
            ly = [yA,yN]
            lx = [xA,xN]
            
            
            plt.title("Notranji urez: Geometrija")
            plt.grid()
            plt.autoscale(enable = True, axis = 'both')
            plt.ylabel("X [m]")
            plt.xlabel("Y [m]")
            plt.scatter(y1,x1, marker = 'o', color = 'b')
            plt.scatter(ny,nx, marker = 'o', color = 'r') #iskano točko obarvamo rdeče!
            plt.plot(y1,x1,'b')
            plt.plot(ly,lx)
            
            #Dodaj napise zraven točk
            plt.text(yA,xA,"A",color = 'k',style = 'normal',fontsize = 11)
            plt.text(yB,xB,"B",color = 'k',style = 'normal', fontsize = 11)
            plt.text(yC,xC,"C",color = 'k',style = 'normal', fontsize = 11)
            plt.text(yN,xN,"N",color = 'r',style = 'normal', fontsize = 11)
            plt.show()
            
            print()
            print("Rezultati:")
            print(" Y = {:.4f}".format(yN))
            print(" X = {:.4f}".format(xN))
            
            #IZPIS REZULTATOV - txt
            
            notranji_rez = open("rezultati.txt", "a")
            
            notranji_rez.write("Notranji urez\n")
            notranji_rez.write("------------------------------------\n")
            notranji_rez.write("Vhodni podatki:\n")
            notranji_rez.write("yA = {:.4f} \n".format(yA))
            notranji_rez.write("xA = {:.4f} \n".format(xA))
            notranji_rez.write("yB = {:.4f} \n".format(yB))
            notranji_rez.write("xB = {:.4f} \n".format(xB))
            notranji_rez.write("yC  = {:.4f} \n".format(yC))
            notranji_rez.write("xC  = {:.4f} \n".format(xC))
            notranji_rez.write("alfa  = {:3.4f} \n".format(rad2dms(alfa)))
            notranji_rez.write("beta  = {:3.4f} \n".format(rad2dms(beta)))
            notranji_rez.write("------------------------------------\n")
            notranji_rez.write("Koordinate nove tocke:\n")
            notranji_rez.write("Y = {:.4f} \n".format(yN))
            notranji_rez.write("X = {:.4f} \n".format(xN))
            notranji_rez.write("------------------------------------\n")
            
            notranji_rez.close()
            
            #IZPIS REZULTATOV - csv
            notranji_csv = open("izracuni.csv", "a")
            notranji_csv.write("Notranji_urez,yA,xA,yB,xB,yC,xC,alfa,beta\n") #header
        
            dec = "{:.4f}," #prvi in ostali
            dec_last = "{:.4f}\n" #zadnji

            notranji_csv.write("Vrednosti,")
            notranji_csv.write(dec.format(yA))
            notranji_csv.write(dec.format(xA))
            notranji_csv.write(dec.format(yB))
            notranji_csv.write(dec.format(xB))
            notranji_csv.write(dec.format(yC))
            notranji_csv.write(dec.format(xC))
            notranji_csv.write(dec.format(alfa))
            notranji_csv.write(dec_last.format(beta))
        
            notranji_csv.close()
            
        else:
            print("Nemogoča geometrija točk.")
        
    elif ((yA or xA) and (yB or xB) and (yC or xC) and (alfa or beta)) > 0.0:
        print("Negativnih koordinat ali smeri ne sprejemam...")
    else:
        print("---")
    
    return
# %% 4. Ločni presek

def locni(yA:float,xA:float,yB:float,xB:float,a:float,b:float):
    
    """Ločni presek uporabimo, kadar imamo namesto merjenih smeri, na voljo merjene razdalje
       od dveh, treh danih točk do nove točke. Postopek lahko izračnamo na dva
       načina, program uporablja trigonometrični način izračuna.
       
    :param yA: Y koordinata prve točke
    :param xA: X koordinata prve točke
    :param yB: Y koordinata druge točke
    :param xB: Y koordinata druge točke
    :param a: razdalja od točke A do nove točke
    :param b: razdalja od točke B do nove točke
    
    :return: Funkcija vrne koordinate nove točke, grafično izriše geometrijo točk in izračunane vrednosti izpiše na *.txt in *csv.
    
    :Example:
    >>>    
    >>> yA = 459100.50
    >>> xA = 99989.58
    >>> yB = 459200.19
    >>> xB = 101340.75
    >>> a = 80.15
    >>> b = 60.88
    >>> locni(yA,xA,yB,xB,a,b)
    """

    if (yA or xA or yB or xB or a or b) > 0.0:
        print("Računam...")
        d = dol(yA,xA,yB,xB)
        
        alfak = ((d**2 + a**2 - b**2)/(2*d*a))
        betak = ((d**2 + b**2 - a**2)/(2*d*b))
        
        alfak = dms2rad(alfak)
        betak = dms2rad(betak)
        
        if (alfak > 2*math.pi):
            alfak = alfak - 2*math.pi
        elif (betak > 2*math.pi):
            betak = betak -2*math.pi
        elif (alfak > 2*math.pi) and (betak > 2*math.pi):
            alfak = alfak - 2*math.pi
            betak = betak -2*math.pi
        else:
            alfak = alfak
            betak = betak
        
        #Cos je treba spravit v definicijsko območje
        def clean_cos(kot):
            return min(1,max(kot,-1))
        
        alfak_clean = clean_cos(alfak)
        betak_clean = clean_cos(betak)
        
            
        alfa_locni = math.acos(alfak_clean)
        beta_locni = math.acos(betak_clean)
        
        if (alfa_locni or beta_locni) < 0.0:
            alfa_locni = alfa_locni + 2*math.pi
            beta_locni = beta_locni + 2*math.pi
        else:
            alfa_locni = alfa_locni
            beta_locni = beta_locni

        #še zaloga vrednosti acos() in asin()
        if ((alfa_locni and beta_locni) < math.pi) or ((alfa_locni and beta_locni) > 0.00):
            print("nadaljujem izračun...")
            #kontrola
            dk = a*math.cos(alfa_locni)+b*math.cos(beta_locni)
            #smerni koti stranic trikotnika
            niAN = ni(yA,xA,yB,xB) + alfa_locni
            niBN = ni(yB,xB,yA,xA) - beta_locni
            #izračun koordinatnih razlik do nove točke N
            delyAN = a*math.sin(niAN)
            delyBN = b*math.sin(niBN)
            delxAN = a*math.cos(niAN)
            delxBN = b*math.cos(niBN)
            #koordinate nove točke N
            yN1 = yA + delyAN
            xN1 = xA + delxAN
            yN2 = yB + delyBN #kontrola
            xN2 = xB + delxBN #kontrola
        
            #Koordinate nove točke
            yN = yN1
            xN = xN1

            #GRAFIČNA PREDSTAVITEV - matplotlib
            
            x1 = [xA,xB,xN]
            y1 = [yA,yB,yN]
            s1 = [xA,xN]
            s2 = [yA,yN]
            
            plt.title("Ločni presek: Geometrija")
            plt.grid(True)
            plt.autoscale(enable = True, axis = 'both')
            plt.ylabel("X [m]")
            plt.xlabel("Y [m]")
            plt.scatter(y1,x1,marker = 'o', color = 'r') 
            plt.plot(y1,x1, "b")
            plt.plot(s2,s1, "b")
            
            #Dodaj napise zraven točk
            plt.text(yA,xA,"A",color = 'k',style = 'normal',fontsize = 11)
            plt.text(yB,xB,"B",color = 'k',style = 'normal',fontsize = 11)
            plt.text(yN,xN,"N",color = 'k',style = 'normal',fontsize = 11)
            plt.show()
            
            #Rezultati
            print("Rezultati: ")
            print(" Y = {:.4f}".format(yN))
            print(" X = {:.4f}".format(xN))
            print()
            
            #IZPIS REZULTATOV - txt
            
            locni_rez = open("rezultati.txt", "a")
            
            locni_rez.write("Locni presek\n")
            locni_rez.write("------------------------------------\n")
            locni_rez.write("Vhodni podatki:\n")
            locni_rez.write("yA = {:.4f} \n".format(yA))
            locni_rez.write("xA = {:.4f} \n".format(xA))
            locni_rez.write("yB = {:.4f} \n".format(yB))
            locni_rez.write("xB = {:.4f} \n".format(xB))
            locni_rez.write("a  = {:.4f} \n".format(a))
            locni_rez.write("b  = {:.4f} \n".format(b))
            locni_rez.write("------------------------------------\n")
            locni_rez.write("Koordinate nove tocke:\n")
            locni_rez.write("yN = {:.4f} \n".format(yN))
            locni_rez.write("xN = {:.4f} \n".format(xN))
            locni_rez.write("------------------------------------\n")
            
            locni_rez.close()
            
            #IZPIS REZULTATOTV - csv
            locni_csv = open("izracuni.csv", "a")
            locni_csv.write("Locni_presek,yA,xA,yB,xB,a,b\n") #header
        
            dec = "{:.4f}," #prvi in ostali
            dec_last = "{:.4f}\n" #zadnji

            locni_csv.write("Vrednosti,")
            locni_csv.write(dec.format(yA))
            locni_csv.write(dec.format(xA))
            locni_csv.write(dec.format(yB))
            locni_csv.write(dec.format(xB))
            locni_csv.write(dec.format(a))
            locni_csv.write(dec_last.format(b))
        
            locni_csv.close()
        
            
        else:
            print("Nerealna geometrija točk. -.- ")
            
    elif (yA or xA or yB or xB or a or b) < 0.0:
        print("Negativnih koordinat ali dolžin ne sprejemam.")
        
    else:
        print("---")
        return
# %%