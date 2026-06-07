Follow the below steps to run YOLO in your rasberry Pi:

1. After installing the Gaashub app, check where the GaasHub App image is present.
2. CD to that folder in a terminal.
3. Now, Open GaasHUb app using the command: ./GaasHub.AppImage --no-sandbox
4. App will open and you need to login
5. Click the power button in the app to connect to GPU
6. Now clone this repository
7. In this repository,input_image folder have the input images. We have provided 3 images, you can use yours too. Just put the image in the input_image folder.
8. Now open new terminal and CD to the folder where you cloned this repository.
9. To run the code, type gaashub . (gaashub space dot), and press enter.
10. It will take few seconds and the YOLO output image will be generated in a new folder in the same path.
11. Congratulations!!, you have run YOLO algorithm in your rasberry pi.
12. Add more images of your own in the input_image folder and YOLO image will be genrated in output_images folder.
