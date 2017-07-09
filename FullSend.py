from subprocess import call
import glob
import os
def Read(nombre):
	list=[]
	for fname in sorted(glob.glob(nombre+'/*.jpg')):
		list.append(fname)
	return list
def Sending(NamePath, folderPath):
    imagenes = Read(NamePath)
    for imagen in imagenes:
        photofile = "gcloud compute copy-files ~/{} DeepMicroSystems@computer-1:~/WORKDIR/{}/  --zone us-central1-b".format(imagen,folderPath)
        call ([photofile], shell=True)
        os.remove(imagen)
folder1 = 'casosReportados'
folder2 = 'placasAreconocer'
Sending('Prueba',folder2)
print('DONE!! sent first folder')