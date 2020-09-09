# import required libraries
from datetime import datetime
import cv2

stream = cv2.VideoCapture(0)

if (stream.isOpened()):
            print("Starting Camera.")

        # define codec and create VideoWriter
CODEC = 'XVID'
FPS = 30
RES = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*CODEC)
date = datetime.now()
out = cv2.VideoWriter('videos/recording_'
                                + str(date.month) + '-'
                                + str(date.day) + '-'
                                + str(date.year) + '_'
                                + str(date.hour) + '-'
                                + str(date.minute) + '-'
                                + str(date.second) + '_'
                                + '.avi', fourcc, FPS, RES, True)
# start the streaming loop
while(stream.isOpened()):
    # capture frame by frame
    ret, frame = stream.read()

    # make sure the frames are reading
    if not ret:
        print("Unable to receive frame.")
        break

    # write the frame
    out.write(frame)

    # show frame
    if True:
        cv2.imshow("Current View", frame)

    # run until key press 'q'
    QUIT_KEY = 'q'
    if cv2.waitKey(1) == ord(QUIT_KEY):
        stream.release()
out.release()
cv2.destroyAllWindows()