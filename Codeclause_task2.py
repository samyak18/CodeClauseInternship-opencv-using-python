import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces
def draw_faces(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
def identify_and_verify_faces(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return
    faces = detect_faces(image)
    if len(faces) == 0:
        print("No faces detected in the image.")
        return
    draw_faces(image, faces)
    cv2.imshow('Detected Faces in Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def identify_and_verify_faces_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file. Please check if the file path is correct.")
        return
    cv2.namedWindow('Detected Faces in Video', cv2.WINDOW_NORMAL)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        faces = detect_faces(frame)
        draw_faces(frame, faces)
        cv2.imshow('Detected Faces in Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
image_path = r'C:\Users\kumar\OneDrive\Desktop\sam.jpg'
identify_and_verify_faces(image_path)
video_path = r"C:\Users\kumar\Downloads\video (240p).mp4"
identify_and_verify_faces_video(video_path)





