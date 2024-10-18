import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json


plt.ion()
bolha_arq = pd.read_csv('labels_bolhas.csv', delimiter=',')['image']
df = pd.read_csv('labels_bolhas.csv', delimiter=',')['label']

for i in range(len(df)) :
   bolha_name = list(str(bolha_arq[(i)]).split('-'))
   del bolha_name[0] 
   bolha_name = str(bolha_name).strip("'[]'")

   
   df_dict = (json.loads(df.iloc[(i)][1:-1]))['points']
   s0 = np.array(df_dict)

   plt.close()
   plt.plot(np.array(list(s0[:,0]*16)+[s0[0,0]*16]),np.array(list(s0[:,1]*1.55)+[s0[0,1]*1.55]),'ro-', linewidth=1.5)
   plt.grid()


# Agora vamos plotar a o perfil da bolha sobre a imagem da bolha 
   import cv2

   imagem = '/home/ml1/Desktop/fotos_tratadas/' + bolha_name
   img = cv2.imread(imagem)

# definimos os valore que serão usados no Polylines (Pontos, se o poligono é fechado, cor e espessura)
   pts = []
   for i in range(len(df_dict)) :
      pts.append((df_dict[i][0]*16,df_dict[i][1]*1.55))
   pts = np.array(pts,np.int32) # Transforma os valore para int para que sejam utilizados 
   IsClosed = True
   cor = (0,0,255) #vermelho em RGB (Valores na ordem : Azul, verde, vermelho)
   espessura = 2 

# Usamos o polylines para desenhar o poligono em cima da imagem 
   cv2.polylines(img, [pts] , IsClosed, cor, espessura)

# Mostramos o resultado
   cv2.imshow(bolha_name[:-4] + "_Perfil", img)
   cv2.waitKey ()
   cv2.destroyAllWindows ()

