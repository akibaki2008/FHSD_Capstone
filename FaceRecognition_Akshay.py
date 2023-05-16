# PACKAGES FROM OPENCV HAS BEEN USED IN MANY ASPECTS.
# FACE RECOGNITION FORM OPENCV ALSO USED PACKAGE FROM GITHUB PACKAGE WEBSITE

#DOCUMENTATION ONLY on package names and package terminology was used from this website:
#https://face-recognition.readthedocs.io/en/latest/face_recognition.html
#   ONLY USED FOR UNDERSTANDING OPENCV PACKAGES AND ITS MEANINGS 

# Documentation for showing cv2 window commands were also used:
#https://www.tutorialkart.com/opencv/python/opencv-python-read-display-image/

import face_recognition
import os, sys
import cv2
import numpy as np
import math



#/////////////////////////////////////////////////////////////////////////
# The faceRecognition class is used to actually perform the facial recognition on a video stream.
# So basically first is initilaizes some variables.
# then after that it basically the encode faced method encodes it and stores the faces in known_face_encodings.

class FaceRecognition:
    locations_of_the_faces = []
    faces_found_encoding = []
    the_names_of_faces = []
    collection_known_faces_encoded = []
    collection_known_faces_name = []
    process_of_the_current_frame = True

    def __init__(self):
        self.encode_faces('faces')
# the encoding done here, is basically the process suggested for these type of projects. Basically
# the encoding from my understanding is when you basically extract a unique set of these numerical features.
# from the face image which opencv package does. I believe, it extracts a 128-dimensional feature vector for.
# each face in the image. Then those features are compares with the predefines images to see if they are same.

    def encode_faces(self, dirName):
        if(os.path.exists(dirName)):
            for image in os.listdir(dirName):
                #note that the os.listdir() is for opening the director that I have made with a picture of elon musk photo
                # and also a picture of zuckerberg and the directory is called faces.
                thefacecompare_image = face_recognition.load_image_file(f"faces/{image}")
                face_encoding = face_recognition.face_encodings(thefacecompare_image)[0]

                #Here, the loaded images are then passed to the face_recognition.face_encodings() function to obtain
                # the face encodings list along with the respective image names in the "known_face_names" list.
                self.collection_known_faces_encoded.append(face_encoding)
                self.collection_known_faces_name.append(image.split('.')[0])
            print(self.collection_known_faces_name)
        else:
            print("Error: Unable to open Predefined Image directory")

    def run_recognition(self):
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')
        if self.collection_known_faces_name.count == 0:
            sys.exit('No pre-defined Faces to Detect, were found in the provided directory.')
            
        while True:
            ret, frame = video_capture.read()

            # Only process every other frame of video to save time
            if self.process_of_the_current_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Finds all the Face_locations with the current Frame
                self.locations_of_the_faces = face_recognition.face_locations(rgb_small_frame)

                # For each of the Located Face co-ordinates, calcaultes the Face_Encoding value, for comparison
                self.faces_found_encoding = face_recognition.face_encodings(rgb_small_frame, self.locations_of_the_faces)

                self.the_names_of_faces = []

              
                for single_found_face in self.faces_found_encoding:                    
                    matches = face_recognition.compare_faces(self.collection_known_faces_encoded, single_found_face)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(self.collection_known_faces_encoded, single_found_face)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = self.collection_known_faces_name[best_match_index]
                    self.the_names_of_faces.append(f'{name}')

            self.process_of_the_current_frame = not self.process_of_the_current_frame

            # Display the results
            for (top, right, bottom, left), name in zip(self.locations_of_the_faces, self.the_names_of_faces):

                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Create the frame with the name
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition()




