import cv2
import os
import datetime

folder: str = '/var/www/html'
frame_height: int = 720
frame_width: int = 1280

ifolder = os.path.join(folder, 'images')
if not os.path.isdir(ifolder):
    os.makedirs(ifolder)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 3)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
try :
    _, frame = cap.read()
    filename: str = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.png'
    filepath: str = os.path.join(ifolder, filename)
    print(filepath + '...')
    cv2.imwrite(filepath, frame)
    print(filepath + '... Done.')
except:
    cap.release()