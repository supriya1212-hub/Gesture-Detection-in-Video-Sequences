
Gesture Detection Prototype

Overview

This prototype aims to detect a specific gesture within a video sequence. The desired gesture is defined by an input image or a short video clip. The task involves analyzing a test video to determine whether the gesture occurs. If the gesture is detected, the prototype overlays the word "DETECTED" in bright green on the top right corner of the output frames.

Input

Desired Gesture Representation: This could be a single image or a short video clip defining the gesture to be detected.
Test Video: A video with random gestures, where the presence of the desired gesture needs to be detected.

Output

Annotated test video frames where the gesture is detected with "DETECTED" in bright green on the top right corner.
The output can be either a processed video or a sequence of annotated frames.
Dependencies

Python 3.x
OpenCV (pip install opencv-python)
NumPy (pip install numpy)


https://github.com/supriya1212-hub/Gesture-Detection-in-Video-Sequences/assets/85392844/5f6e4e6a-238b-4663-8afb-34acbd210ebf


Notes: 

Ensure that the test video contains a variety of gestures, including variations of the desired gesture to be detected.
Experiment with different threshold values and template matching techniques for optimal detection accuracy.
For better performance, consider resizing the input frames and templates before performing template matching.
