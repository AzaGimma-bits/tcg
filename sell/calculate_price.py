

def sum_price():
    with open("fedo.txt", 'r') as text:
        #print(text.readlines())
        total=0
        for linea in text:
            for indice in range(len(linea)):
                caracter = linea[indice]
                if caracter == '\t' and (linea[indice+1]).isnumeric() == True:
                    n=1
                    num=''
                    while linea[indice+n] != '\n': 
                        num_temp = str(linea[indice+n])
                        num = num + num_temp                    
                        n=n+1
                    total=float(num)+float(total)
                    print(total)
                    
                    #print(linea[indice+1])
                #print(caracter)
sum_price()             