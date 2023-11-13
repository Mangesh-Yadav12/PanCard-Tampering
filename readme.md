##PanCard Tempering
Problem Statement:
The purpose of this project is to detect tampering of PAN cards using computer vision. This project will help different organizations in detecting whether the ID i.e. the PAN card provided to them by their employees or customers or anyone is original or not.
For this project, we will calculate the structural similarity of the original PAN card and the PAN card uploaded by the user.

Summary:
Finding out structural similarity of the images helped us in finding the difference or similarity in the shape of the images. Similarly, finding out the threshold and contours based on those thresholds for the images converted into grayscale binary also helped us in shape analysis and recognition.
As our SSIM is ~31.2% we can say that the image the user provided is fake or tampered with.
Finally, we visualized the differences and similarities between the images by displaying the images with contours, differences, and thresholds.

Scope:
This project can be used in different organizations where customers or users need to provide any kind of ID to get themselves verified. The organization can use this project to find out whether the ID is original or fake. Similarly, this can be used for any type of ID like Adhar, voter ID, etc.
