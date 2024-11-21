import socket
import os
import cv2
from cvzone.HandTrackingModule import HandDetector

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize camera and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)

def get_directions():
    
    ret, frame = cap.read()
    if not ret:
        return "camera_error"

    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame)
    direction = 'stop'  # Default state

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Map hand gestures to directions
        if fingers == [1, 0, 0, 0, 0]:
            direction = 'left'
        elif fingers == [0, 0, 0, 0, 1]:
            direction = 'right'
        elif fingers == [1, 1, 0, 0, 1]:
            direction = 'spin'
        elif fingers == [0, 1, 0, 0, 0]:
            direction = 'forward'
        elif fingers == [0, 1, 1, 0, 0]:
            direction = 'backward'
        elif fingers == [0, 1, 0, 0, 1]:
            direction = 'uturn'

    # Display the frame with hand detection
    cv2.imshow("Frame", frame)
    return direction

if __name__ == '__main__':
    host ='ip_adress' # write the ip adress on which you are using camera that is server 
    port = 5000         # Port to listen on

    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the address and port
        s.bind((host, port))
        s.listen(1)
        print(f"Server started. Listening on {host}:{port}...")
        print("Waiting for a client to connect...")

        # Wait for client connection
        c, addr = s.accept()
        print(f"Connection established with {addr}")

        while True:
            # Get direction based on hand gestures
            msg = get_directions()

            # Send direction to client
            c.send(msg.encode())

            # Break the loop on pressing 'ESC'
            if cv2.waitKey(1) & 0xFF == 27:
                print("Exiting...")
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up resources
        print("Closing connection and releasing resources...")
        c.close()
        s.close()
        cap.release()
        cv2.destroyAllWindows()
