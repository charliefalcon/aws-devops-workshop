user_input = input("Enter a number between 1 and 3999 : ").strip()

if user_input.isalpha() or user_input == "0":
    
    print ("Your input is not a valid number between 1 and 3999")

elif user_input >= "4000" or user_input < "1" :
    
    print ("Your input is not between 1 and 3999")

else:
    user_input = int(user_input)
    
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV", "I"]
    
    number_roman = ''
    
    number_decimal = user_input
    
    i = 0
    
    while  user_input > 0:
	    
        for j in range(user_input // val[i]):
	        
            number_roman += syb[i]
	        
            user_input -= val[i]
	    
        i += 1
    
    print ("Number", number_decimal, "equals to ", number_roman, "in Roman Numerals")
