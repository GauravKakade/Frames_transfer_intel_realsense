from vidgear.gears import NetGear
import cv2
import imagiz

#imagiz part
server=imagiz.Server()

#vidgear part
#define netgear client with `receive_mode = True` and default settings
options = {"flag": 0, "copy": False, "track": False}

client = NetGear(
    address="192.168.1.213",
    port="3456",
    protocol="tcp",
    pattern=0,
    receive_mode=True,
    logging=True,
    **options
)

# infinite loop
while True:
    # receive frames from network
    frame = client.recv() #vidgear
    message = server.receive()
    frame2 = cv2.imdecode(message.image, 1)


    # check if frame is None
    if frame is None:
        #if True break the infinite loop
        break

    # do something with frame here

    # Show output window
    cv2.imshow("RGB", frame2)
    cv2.imshow("Depth", frame)
    cv2.waitKey(1)

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break

# close output window
cv2.destroyAllWindows()
# safely close client
client.close()
