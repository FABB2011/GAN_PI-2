# GAN_PI-2
fourier3.py lit un fichier WAV, applique la transformée de fourier réelle sur chaques 60èmes de seconde du fichier et créé un
JSON pour chacuns de ces 60ème.

cli.py prend en entrée un ensembe de fichiers JSON et créé une image pour chacuns en utilisant la fonction gan.
Il assemble ensuite chacunes des images ainsi créés en une vidéo.
