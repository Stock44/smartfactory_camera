import time

from CameraSystem import CameraSystem
from PersonDetector import PersonDetector


def main():
    detector = PersonDetector()

    cam = CameraSystem((0.55,0.01,0.09), (0.3,0.01,0), detector, True, address='10.22.240.55', port=80,
                       user='admin', password='L22F0A5E')
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()