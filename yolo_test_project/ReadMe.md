Follow the below steps to run YOLO in your rasberry Pi:

After installing the Gaashub app, check where the GaasHub App image is present.
CD to that folder in a terminal.
Now, Open GaasHUb app using the command: ./GaasHub.AppImage --no-sandbox
App will open and you need to login
Click the power button in the app to connect to GPU
Now clone this repository
In this repository,input_image folder have the input images. We have provided 3 images, you can use yours too. Just put the image in the input_image folder.
Now open new terminal and CD to the folder where you cloned this repository.
To run the code, type gaashub . (gaashub space dot), and press enter.
It will take few seconds and the YOLO output image will be generated in a new folder in the same path.
Congratulations!!, you have run YOLO algorithm in your rasberry pi.
Add more images of your own in the input_image folder and YOLO image will be genrated in output_images folder.
