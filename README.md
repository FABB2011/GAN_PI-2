# GAN_PI-2

This program can create a video clip from an audio file.
The generated clip adapt himself to the fraquencies and the rythm of the chosen track.

# How to use it

Launch "main.py".

Select an audio track :

You can add your own audio track bu adding it in the "audioFiles" folder.
When you launch the code, you can choose your audi file among those of the "audioFiles" folder.

Select a framerate :

You can choose the number of images generated for each second of the chosen audio file.
We recommand 60 and it can not work above this value.

Transitions images :

You will be asked to choose the number of transition images.
The transition images are created to smooth the video.

If you don't want transition images then choose 0.

The choice of the number of transition images will depend on the framerate. 
For a good compromise between a dynamic and a fluid video 20 images of transition for a framerate of 60 is a good choice (For a framerate of 30, it will be 10 transition images, you have to keep the same ratio).

Number of images :

The image structures used to create new images from the audio come from the website Artbreeder (https://www.artbreeder.com).
We collected different types of image from this website and they are stored in the script "classes.py".
We ask the user the number of images he wants to use to make the video.
The user can add his own images in "classes.py".

# How the code work

Fourier transform :

Firstly we use the Fourier transform to compute the frequency response of the audio. 
The Fourier transform is applied on each parts of the audio track in function of the framerate (for exemple if the audio is 1 seconds long and the framerate is 24, we will compute the Fourier transform 24 times.

Exponential moving average :

In order to smooth the frequency response and obtain a fluid video, we use the exponential moving average that will smooth
the signal.

Normalization :

The GAN function that we will use later take value between -1 and 1. If lower or greater values are used, the resulting
images are strange. Therefore, we normalize the data between these two values.

Image type attribution :

We use K-mean clustering to give an image type (a class) to each part of the audio file. For example, if the user chose to use 4 different type of images, the clustering will be compute with 4 clusters.

Image creation :

To create the images we inject our data in the GAN function. Three parameters are given to the GAN function: the "latent space" defined by the audio smoothed and normalized frequencies, the "class" of the image define by the clustering and another parameter called "truncation" that is different for each classes.

The programm will run as following : if the class of N is the same as the class of N + 1, we create the image. If not, we generate transition images between N and N + the number of transitions chosen by the user.

Video creation :
Finally we put together all the created images in one video and we add the chosen audio track and we add it on the video.












