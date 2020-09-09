milisaniye = input("Please enter the milliseconds (should be written in numbers and greater than zero): ")
milisaniye = int(milisaniye)
def hesap():
    saniye =(milisaniye/1000)
    saniye = int(saniye)
    dakika=(milisaniye/(1000*60))%60
    dakika = int(dakika)
    saat=(milisaniye/(1000*60*60))%24
    
    if milisaniye <= 0:
        print ("Not Valid Input !!!. Please enter the milliseconds (should be written in numbers and greater than zero):")
    elif saat==0 and dakika > 0 and saniye > 0:
        print ("%d:%d" % ( dakika, saniye))
    elif dakika==0 and saniye >0:
        print ("%d" % ( saniye))
    elif input==("exit"):
        print ("Exiting the program... Good Bye")
    else:
        print ("%d:%d:%d" % (saat, dakika, saniye))

    return
   
hesap()