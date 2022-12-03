import cv2


def main():
    capture = capture_write()


def capture_write(filename="image.jpeg", port=0, ramp_frames=30, x=1280, y=720):
    camera = cv2.VideoCapture(port)

    # Set Resolution
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, x)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, y)

    # Adjust camera lighting
    for i in range(ramp_frames):
        temp = camera.read()
    
    while 1:
        retval, im = camera.read()
        camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        cv2.imshow('running camera',im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.imwrite(filename,im)
    camera.release()
    del(camera)
    return True

if __name__ == '__main__':
    main()
