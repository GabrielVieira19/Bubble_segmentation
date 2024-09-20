import numpy as np
import os 

pastas = os.listdir('/home/ml1/Desktop/runs/segment')
k = 0  
r = 1
for i in pastas : 

    # definição das pastas onde estão os labels obtidos do predict YOLO 
    pasta = '/home/ml1/Desktop/runs/segment/' + i 
    range_predict = len(os.listdir(pasta+'/labels'))
    first = [136,111,128,121,143]

    #criação do arquivo e escrita do cabeçalho 
    #arquivo = open (pasta + "/comprimentos_bolhas.txt", 'w')
    #cabecalho = 'Comprimento de cada bolha detectada no vídeo \n'
    #arquivo.write(cabecalho)
    
    # Extração das coordenadas de X para cada .txt de cada bolha 
    for j in range(first[k],(range_predict+first[k])) : 
        with open('/home/ml1/Desktop/runs/segment/' + i + '/labels/' + 'bolha' + str(j) + '.txt' , 'r') as file:
            arq = file.read()

        coordinates = []
        
        parts = arq.strip().split()
        x_coordinates = map(float, parts[1:len(parts):4])
        x_real = [(j * 1600)*0.156 for j in x_coordinates] #multiplicamos por 1600 pois é a largura da imagem
        coordinates.append((x_real))

        #coordinates = np.array(coordinates)
        #print('coordenadas', coordinates)

        max = np.amax(coordinates)
        min = np.amin(coordinates)

        #print('valor max de X eh : ', max)
        #print('valor min de X eh : ', min)

        comprimento = max - min 
        comprimento = np.round(comprimento, 3)

        print ('comprimento da bolha' , j , 'eh : ', comprimento)

        arquivo = open (pasta + "/comprimentos_bolhas.txt", 'a')
        info = str(r) + ' : ' +  str(comprimento) + '\n'
        arquivo.write(info)
    r += 1 
    k += 1 
