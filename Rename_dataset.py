import os

#Algoritmo para renomear as imagens e labels que tiramos do Label-Studio, apenas por questão de organização 
path_images = '/home/ml1/Desktop/images'
path_labels = '/home/ml1/Desktop/labels'
imgs = os.listdir(path_images)
labels = os.listdir(path_labels)
n_aux = 50


for i in imgs : 
    if i[:-7] != 'img_bolha' : 
        os.rename(path_images + '/' + i , path_images + '/img_bolha_' + str(n_aux) + '.jpg')
        os.rename(path_labels + '/' + i[:-3] + 'txt' , path_labels + '/label_bolha_' + str(n_aux) + '.txt')
        n_aux += 1 
    else : 
        os.rename(path_images + '/' + i , path_images + '/img_bolha_' + str(n_aux) + '.jpg')
        os.rename(path_labels + '/' + 'label' + i[3:-3] + 'txt' , path_labels + '/label_bolha_' + str(n_aux) + '.txt')
        n_aux += 1 