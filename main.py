import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize video capture and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Variables to track mouth opens and scrolling
mouth_open = False
mouth_open_count = 0
last_mouth_state_change = 0
left_eye_blink = False
right_eye_blink = False
message = ""

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Eye tracking for mouse control
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

        # Blink detection for clicking and messages
        left = [landmarks[145], landmarks[159]]
        right = [landmarks[374], landmarks[386]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)
        
        # Blink detection for left eye
        if (left[0].y - left[1].y) < 0.004:
            if not left_eye_blink:
                left_eye_blink = True
                message = "Welcome to Eye tracker app"
                print(message)
        else:
            left_eye_blink = False
        
        # Blink detection for right eye
        if (right[0].y - right[1].y) < 0.004:
            if not right_eye_blink:
                right_eye_blink = True
                message = "Thanks for watching my demo"
                print(message)
        else:
            right_eye_blink = False

        # Mouth tracking for scrolling and app close
        upper_lip = landmarks[13]
        lower_lip = landmarks[14]
        upper_lip_y = int(upper_lip.y * frame_h)
        lower_lip_y = int(lower_lip.y * frame_h)
        
        # Draw circles on upper and lower lips
        cv2.circle(frame, (int(upper_lip.x * frame_w), upper_lip_y), 3, (255, 0, 0), -1)
        cv2.circle(frame, (int(lower_lip.x * frame_w), lower_lip_y), 3, (255, 0, 0), -1)
        
        # Implement scrolling based on lip distance
        lip_distance = lower_lip_y - upper_lip_y
        current_time = time.time()
        
        if lip_distance > 20:  # Mouth open threshold
            if not mouth_open:
                mouth_open = True
                mouth_open_count += 1
                last_mouth_state_change = current_time

        if lip_distance < 15:  # Mouth close threshold
            if mouth_open:
                mouth_open = False
                if current_time - last_mouth_state_change < 2:  # Scroll if mouth closes within 2 seconds
                    pyautogui.scroll(10)  # Adjust the scrolling amount as needed
                    last_mouth_state_change = current_time

        # Scroll down based on another mouth movement pattern
        if lip_distance < 10:
            pyautogui.scroll(-10)  # Adjust the scrolling amount as needed

        # Close the window if mouth opens twice
        if mouth_open_count == 2:
            break

    # Display message on frame
    if message:
        cv2.putText(frame, message, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Eye and Mouth Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cam.release()
cv2.destroyAllWindows()

# Code Explanation 

# This Python script creates an eye and mouth-controlled mouse system using computer vision techniques. Here's a detailed breakdown of the entire code:

# Import necessary libraries:

# cv2 (OpenCV) for image processing and webcam capture
# mediapipe for face mesh detection
# pyautogui for mouse control and screen interaction
# time for time-based operations


# Initialize the webcam capture (cv2.VideoCapture(0)) and MediaPipe's face mesh model (mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)).
# Get screen dimensions using pyautogui.size().
# Set up variables to track:

# Mouth state (open/closed)
# Mouth open count
# Last mouth state change time
# Left and right eye blink states
# Message to display


# Enter the main loop, which runs continuously:
# a. Capture a frame from the webcam
# b. Flip the frame horizontally for a mirror effect
# c. Convert the frame from BGR to RGB color space
# d. Process the frame with the face mesh model
# e. Get landmark points from the processed output
# If landmark points are detected:
# a. Eye tracking for mouse control:

# Use landmarks 474-478 to track eye movement
# Map eye position to screen coordinates
# Move the mouse cursor using pyautogui.moveTo()

# b. Blink detection:

# Monitor landmarks 145, 159 for left eye and 374, 386 for right eye
# Detect blinks by measuring vertical distance between landmarks
# Set messages based on blink detection ("Welcome to Eye tracker app" for left eye, "Thanks for watching my demo" for right eye)

# c. Mouth tracking for scrolling and app control:

# Use landmarks 13 (upper lip) and 14 (lower lip)
# Calculate lip distance
# Implement scrolling based on mouth movements:

# Scroll up when mouth opens then closes within 2 seconds
# Scroll down when lip distance is very small


# Track mouth open count (used to close the app)


# Display the processed frame:

# Draw circles on detected landmarks
# Display any set messages on the frame
# Show the frame in a window named 'Eye and Mouth Controlled Mouse'


# Check for exit conditions:

# Break the loop if the mouth has been opened twice
# Allow user to exit by pressing 'Esc' key


# After the loop ends, release the webcam and close all OpenCV windows

# Key features of this system:

# Eye movement controls mouse cursor position
# Eye blinks trigger welcome messages
# Mouth movements control scrolling:

# Opening and quickly closing mouth scrolls up
# Very small lip distance scrolls down


# Opening mouth twice exits the application

# This code demonstrates an innovative way to interact with a computer using facial movements, combining computer vision techniques with user interface control. It showcases the potential of using MediaPipe's face mesh for creating accessible interfaces or novel interaction methods.
# The system could be further improved by adding more gestures, refining the detection thresholds, or incorporating machine learning for more accurate and personalized gesture recognition.