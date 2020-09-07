# import required libraries
from vidgear.gears import NetGear
from datetime import datetime
import cv2

# define tweak flags
options = {'flag' : 0, 'copy' : False, 'track' : False}

# Define Netgear Client at given IP address and define parameters (!!! change following IP address '192.168.x.xxx' with yours !!!)
client = NetGear(address = '172.16.4.182', port = '5454', protocol = 'tcp',  pattern = 0, receive_mode = True, logging = True, **options)

# loop over
while True:

    # receive frames from network
    frame = client.recv()

    # check for received frame if Nonetype
    if frame is None:
        break

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()