# EyeTrackPy
EyeTrackPy is a Python-based algorithm designed to track and analyze eye movements in real time using computer vision techniques. 
Certainly! Here's a detailed description, implementation overview, and tech stack for your eye tracker algorithm project.

### **Project Description**

**`EyeTrackPy`** is an advanced eye-tracking algorithm developed in Python that enables real-time tracking and analysis of eye movements. By leveraging cutting-edge computer vision techniques, the algorithm detects facial landmarks, isolates the eye regions, and tracks the direction of the gaze with high precision. This project is designed to be highly adaptable, making it suitable for various applications such as user experience research, accessibility tools, human-computer interaction, and gaming.

### **Implementation Overview**

The implementation of **`EyeTrackPy`** involves several key steps:

1. **Facial Landmark Detection:**
   - The algorithm first detects the face within a video frame using a pre-trained model.
   - It then identifies key facial landmarks, focusing on the regions around the eyes.

2. **Eye Region Extraction:**
   - Once the eye regions are identified, they are extracted for further processing.
   - The extracted eye regions are analyzed to detect the position of the pupil.

3. **Gaze Estimation:**
   - The position of the pupils is tracked over time to estimate the direction of the gaze.
   - The algorithm uses geometric transformations and image processing techniques to determine where the user is looking.

4. **Real-Time Processing:**
   - The entire process is optimized for real-time performance, ensuring that the eye movements are tracked smoothly without significant delays.
   - The results can be visualized or integrated into other applications, depending on the use case.

### **Tech Stack**

- **Programming Language:** Python 3.x
- **Libraries:**
  - **OpenCV:** Used for image processing and real-time computer vision tasks.
  - **Dlib:** Employed for facial landmark detection, providing robust and accurate facial feature tracking.
  - **NumPy:** Utilized for efficient numerical operations, especially for handling image arrays and computations.
  - **SciPy:** Provides additional scientific computation tools, particularly for image manipulation and geometric transformations.
  - **Matplotlib (Optional):** Can be used for visualizing the results, such as plotting the gaze direction over time.

This setup ensures that **`EyeTrackPy`** is both powerful and flexible, capable of handling complex eye-tracking tasks in a wide range of environments.
# Screenshots

![Screenshot (227)](https://github.com/user-attachments/assets/c4d55d94-fb96-4ede-a821-9483ecde1139)
![Screenshot (228)](https://github.com/user-attachments/assets/a9ad3301-83c4-4ec0-9d50-2f99a4b44b9e)
![Screenshot (229)](https://github.com/user-attachments/assets/5f01![Screenshot (230)](https://github.com/user-attachments/assets/7cdefe2d-f8d9-4718-acd2-017beea83a91)
7d81-e624-4418-8443-e4bcc8c8a9d6)
