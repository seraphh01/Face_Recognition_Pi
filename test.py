import os
import cv2
import face_recognition
import sys
import pickle


def draw_face_locations(img, face_locations, color=(0, 0, 255)):
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(img, (left, top), (right, bottom), color, 2)


def train():
    # Load known face encodings
    known_faces = []
    for img_name in os.listdir('known_faces'):
        img_path = os.path.join('known_faces', img_name)
        img = face_recognition.load_image_file(img_path)
        img_encoding = face_recognition.face_encodings(img)[0]
        known_faces.append(img_encoding)

    pickle.dump(known_faces, open('known_faces.dat', 'wb'))
    pass


def test(frame):
    known_faces = pickle.load(open('known_faces.dat', 'rb'))

    try:

        # Find all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Compare faces in the frame with known faces
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            if True in matches:
                print("Face detected")
                draw_face_locations(frame, face_locations, (0, 255, 0))
            else:
                print("No face detected")
                draw_face_locations(frame, face_locations, (0, 0, 255))

        if len(face_encodings) == 0:
            print("No face detected")

        # Display the resulting frame
        cv2.imwrite('test_result.jpg', frame)

    except Exception as e:
        print(f"No face detected or an error occured! {e}")


def test_cam():
    # cam = cv2.VideoCapture('video.mp4')
    # cam = cv2.VideoCapture(0)
    cam = cv2.VideoCapture('http://192.168.100.36:4747/mjpegfeed?640x480')

    result, frame = cam.read()

    if not result:
        print("Cannot read camera frame")
        sys.exit(1)

    test(frame)


def test_file(filename='test_known.jpg'):
    frame = cv2.imread(filename)
    if frame is None:
        print(f"Cannot read file {filename}")
        sys.exit(1)
    test(frame)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'train':
            train()
        elif sys.argv[1] == 'test':
            if len(sys.argv) > 2:
                if sys.argv[2] == 'camera':
                    test_cam()
                else:
                    test_file(sys.argv[2])
            else:
                test_file()
        else:
            print("Usage: python test.py [train|test] [filename/camera]")
    else:
        print("Usage: python test.py [train|test] [filename/camera]")
