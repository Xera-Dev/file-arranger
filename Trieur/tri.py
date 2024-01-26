import os
import shutil

class DirCleaner:
        
    def cleaner(self):
        get_dir = os.getcwd()   #Avoir le chemin du "current directory"
        #création des dossiers
        pdfs = os.getcwd() + '\\Pdfs'  
        textes = os.getcwd() + '\\textes'
        images = os.getcwd() + '\\images'
        videos = os.getcwd() + '\\vidéos'
        logiciels = os.getcwd() + '\\logiciels'
        archives = os.getcwd() + '\\archives'
        musiques = os.getcwd() + '\\musiques'
        autres = os.getcwd() + '\\autres'
        
        try:
            os.mkdir(pdfs)
            os.mkdir(textes)
            os.mkdir(images)
            os.mkdir(videos)
            os.mkdir(logiciels)
            os.mkdir(archives)
            os.mkdir(musiques)
            os.mkdir(autres)

        except : pass
        #Ici nous allons parcourir les fichiers qui sont dans le dossier et les sous-dossiers du répértoir actuel
        for chemin, sous_rep, fichiers in os.walk(get_dir):
            for fichier in fichiers :
                new_path = os.path.join(chemin, fichier)
                #Selon l'extention du fichier, nous allons le placer dans le dossier approprié
                if new_path.endswith("pdf"):
                    try:
                        shutil.move(new_path,pdfs)
                    except : pass
                elif new_path.endswith("txt") or new_path.endswith(".odt") or new_path.endswith("docx")  or new_path.endswith("doc"):
                    try:
                        shutil.move(new_path,textes)
                    except : pass
                elif new_path.endswith("jpeg") or new_path.endswith("jpg") or new_path.endswith("png") or new_path.endswith("psd"):
                    try:
                        shutil.move(new_path,images)
                    except : pass
                elif new_path.endswith("mp4") or new_path.endswith("avi") or new_path.endswith("mov") or new_path.endswith("flv") or new_path.endswith("mkv") or new_path.endswith("wmv"):
                    try:
                        shutil.move(new_path,videos)
                    except : pass
                elif new_path.endswith("msi") or new_path.endswith("exe") or new_path.endswith("bat"):
                    try:
                        shutil.move(new_path,logiciels)
                    except : pass 
                elif new_path.endswith("zip") or new_path.endswith("rar") or new_path.endswith("iso"):
                    try:
                        shutil.move(new_path,archives)
                    except : pass
                elif new_path.endswith("flac") or new_path.endswith("wav") or new_path.endswith("mp3"):
                    try:
                        shutil.move(new_path,musiques)
                    except : pass
                else:
                    try:
                        shutil.move(new_path,autres)
                    except : pass
            for dossier  in sous_rep:

                print("nous cherchons dans le dossier : ", dossier + " ... \n ")
        print("Votre dossier est en cours de rangement :D ")
            

if __name__ == "__main__":
    InstanceOfCleaner = DirCleaner()
    InstanceOfCleaner.cleaner()