import cv2
import os 



folder_path = '/home/ml1/Desktop/fotos_tratadas/Teste_comprimento/'
videos = os.listdir('/home/ml1/Desktop/video_bolhas/Teste_comprimento/')
coordenadas_corte = []
videos_ignorados = ''


for i in videos : 
  angulação = 0.0 
  coordenadas_corte = []
  n_pasta = i[3:-4]
  num_img = 0 #Variável auxiliar para mudar entre as fotos 

  pasta_fotos_geral = os.listdir("/home/ml1/Desktop/fotos_bolha/Teste_comprimento/") #Listar todas as as pastas dos diferentes vídeos
  pasta_fotos = os.listdir("/home/ml1/Desktop/fotos_bolha/Teste_comprimento/" + 'fotos' + n_pasta) #listar todas as fotos de cada pastas espefícica
  quant_img = len(pasta_fotos) #Quantidade de fotos que temos na pasta 

  print ("Fotos do vídeo: " + i + " prontas para processamento =" , quant_img)
  ignorar_video = str(input("deseja ignorar o tratamento desse vídeo em específico ? "))
  if ignorar_video == 'sim' or ignorar_video == 'Sim' :
    videos_ignorados = "sim"
    continue

  #Criar uma nova pasta para armazenar as fotos já processadas  
  try : 
    if not os.path.exists(folder_path + 'tratadas' + n_pasta):
      new_folder = folder_path +'tratadas' + n_pasta
      os.makedirs(new_folder)
    if os.path.exists(folder_path + n_pasta) :
      print ("Pasta 'tratadas" + n_pasta + "' já criada !")
      new_folder = folder_path +'tratadas' + n_pasta
  except OSError :
      print("Erro ao criar a pasta")
      new_folder = folder_path +'tratadas' + n_pasta


  for imagens in pasta_fotos : #usamos uma lógica de contador para que todas as imagens sejam trabalhadas

    #Definimos a imagem a ser trabalhada 
    img = cv2.imread('/home/ml1/Desktop/fotos_bolha/Teste_comprimento/' + 'fotos' + n_pasta + '/frame' + str(num_img) + '.jpg')
    
    #Definimos seus parâmetros
    altura, largura = img.shape[:2]
    #print ("Dimensões da imagem :", altura, "x", largura) --> Para saber quais as dimensões 

    #Definimos um ponto para referência de rotação 
    ponto_ref = (largura/2, altura/2) #ponto central da figura 
    if angulação == 0.0 :
      angulação = float(input('Defina qual a angulação do corte ')) #melhor angulação 
    else : 
      angulação = angulação 
    rotacao = cv2.getRotationMatrix2D (ponto_ref, angulação, 0.85) # os parâmetros são: Ponto de referência, angulo de rotação e proporção usada. 
    img_rotacionada = cv2.warpAffine (img, rotacao, (largura, altura))

    #mostramos o resultado da rotação 
    #cv2.imshow("Imagem Rotacionada" + str(num_img), img_rotacionada) # --> Caso queiramos ver imagem por imagem, tirar da forma de comentário
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #Agora precisamos recortar a imagem para visualizar apenas o necessário
    if len(coordenadas_corte) == 0 :
      coordenadas_corte = str(input("Defina a região de interesse para o recorte, 4 valores na forma de 'x,y,w,h' : "))
      coordenadas_corte = coordenadas_corte.split(sep=',')

    #Definimos uma região de interesse (um retângulo que melhor recorta a tubulação)
    x = int(coordenadas_corte[0])
    y = int(coordenadas_corte[1])
    w = int(coordenadas_corte[2]) 
    h = int(coordenadas_corte[3])  
    recorte = img_rotacionada[y:y+h,x:x+w]

    if num_img == 0 : #Para ver ter uma amostra de como ficará a imagem 
      cv2.imshow("Amostra",recorte) #--> Caso queiramos ver imagem por imagem, tirar da forma de comentário
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      continuar = str(input("continuar com o tratamente usando essas configurações ? Responder utilizando 'sim' ! "))
      if continuar != 'sim' : 
        break
        
    nome_tratada = folder_path + 'tratadas' +n_pasta + '/bolha' + str(num_img) + '.jpg'

    #Passamos para tons de cinza para melhores resultados
    gray = cv2.cvtColor(recorte, cv2.COLOR_BGR2GRAY)

    #Antes de salvar, fazemos um último tratamento na imagem, equalizando o histograma da imagem e reduzindo os ruídos (Denoising)
    tratada = cv2.equalizeHist(gray)
    tratada = cv2.fastNlMeansDenoising(tratada)
    

    #Criamos um arquivo txt para guardar as configurações usadas no tratamento, guardamos a angulação e a região de interesse
    if num_img != 0 :
      arquivo = open (new_folder + "/configuração_tratamento.txt", 'w+')
      info = "Angulação do corte = " + str(angulação) + ' ; \n' 'Coordenadas da região de interesse = ' + str(x) + ', ' + str(y) + ', ' + str(w)  + ', ' + str(h)
      arquivo.write(info)
      
    #Vamos salvar cada imagem tratada na pasta 'fotos_tratadas' de cada vídeo e também na pasta geral
    cv2.imwrite(nome_tratada, tratada)
    print("Salvando..." + nome_tratada)
    num_img += 1 
