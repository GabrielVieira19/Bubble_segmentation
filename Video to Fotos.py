import cv2 
import os 

teste = int(input("Qual a finalidade das imagens ? \n 1)Imagens para Treinamento. \n 2)Imagens para Teste. \n"))

if (teste == 1) :
    finalidade = 'Treinamento/'
else : 
    finalidade = 'Teste/'

#Seleciona qual vídeo será exibido
folder_path = '/home/ml1/Desktop/fotos_bolha/' + finalidade + 'fotos'
videos = os.listdir ('/home/ml1/Desktop/video_bolhas/' + finalidade)
for i in videos : 
    n_pasta = i[3:-4]
    video = '/home/ml1/Desktop/video_bolhas/' + finalidade + i
    cap = cv2.VideoCapture(video) 

#Se o vídeo não for aberto pelo programa, exibe mensagem de erro
    if (cap.isOpened()== False) :
        print("Erro ao abrir o vídeo") 
    else :
        print("Video aberto corretamento, rodando video : " + i)

#Vamos criar a pasta para armazenar as fotos retiradas do vídeo 
    try : 
        if not os.path.exists(folder_path + n_pasta):
            os.makedirs(folder_path + n_pasta)
        if os.path.exists(folder_path + n_pasta) :
            print ("Pasta já criada !")
            new_folder = folder_path + n_pasta
    except OSError :
        print("Erro ao criar a pasta")

    if len(os.listdir(new_folder)) != 0 : 
        substituir = str(input("Pasta já contém fotos, deseja substituí-las ? Favor responder com 'Sim' ou 'Nao' ! "))
        if substituir == 'Sim' or substituir == 'sim': 
            print("Substituição requerida...")
        else :
            continue
    
    frames_totais = 0     
    frame_inicial = 0
    frames_atuais = 0

#Para saber quantos frames o vídeo inteiro possui
    while(True) :
        ret, frame = cap.read() 
        if ret :
            frames_totais += 1
        else :
            break

    print ("Quantidades de frames no vídeo inteiro =", frames_totais)
    quant_requerida = int(input("Informe a quantidade de imagens necessárias  "))
    if quant_requerida > frames_totais : 
        quant_requerida = int(input("Quantidade inválida, forneça um número entre 0 e " + str(frames_totais) + " "))
    comeco = int(input("A partir de qual frame começar ?  "))
    if comeco < 0 :
        comeco = int(input("Início inválido, forneça um início maior ou igual a 0  "))

#Aquisição das imagens requeridas 
    cap = cv2.VideoCapture(video)
    while(frames_atuais < quant_requerida): 
        ret, frame = cap.read() 
        
        if ret and frame_inicial > comeco and frames_atuais < quant_requerida: 
            nome_foto = new_folder + '/frame' + str(frames_atuais) + '.jpg'
            print ("Criando..." + nome_foto)
                
            #Agora precisamos salvar essa foto, usando CV2 write
            cv2.imwrite(nome_foto, frame)
                
            frames_atuais += 1

        else :
            frame_inicial += 1
    

