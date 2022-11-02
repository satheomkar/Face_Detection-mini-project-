import cv2
import img_capture
import tkinter
tab=tkinter.Tk()
tab.title("Face Count")
tab.geometry("400x250")
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
#cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    img = cv2.imread('captured_img.png') #cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
    # Display
    cv2.imshow('img', img)
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    #print(count)
    label=tkinter.Label(tab,text=count,font=("Arial", 100))
    label.pack()
    label=tkinter.Label(tab,text=" Faces Destected ",font=("Arial", 30))
    label.pack()
    break
    
tkinter.mainloop()
# Release the VideoCapture object
#cap.release()
