import cv2

def task1():
    image = cv2.imread("variant-10.jpg")
    while True:
        cv2.imshow('image', image) 
        if cv2.waitKey(1) == 27: 
            break
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        thresh,im_bw = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        cv2.imshow('Binary image', im_bw) 
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def task2():
    Img_angle=0
    cap = cv2.VideoCapture("sample.mp4")
    while cv2.waitKey(1) != 27:
        ret, image = cap.read()   
        if not ret:
            break
        mask = cv2.inRange(image, (80, 80, 80), (255, 255, 255))
        ret, thresh = cv2.threshold(mask, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task3():
    Img_angle=0
    cap = cv2.VideoCapture("sample.mp4")
    while cv2.waitKey(1) != 27:
        ret, image = cap.read()
        if Img_angle==1:
            image=cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE )
            Img_angle=0
        if not ret:
            break
        height, width = image.shape[:2]
        mask = cv2.inRange(image, (80, 80, 80), (255, 255, 255))
        ret, thresh = cv2.threshold(mask, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(image, (width//2-150//2, height//2-150//2), (width//2+150//2, height//2+150//2), (0, 255, 255), 2)
        if (x>=(width//2-150//2)) and (y>=(height//2-150//2)) and ((x + w)<=(width//2+150//2)) and ((y + h)<=(height//2+150//2)):
            Img_angle=1
        cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def additional_task():
    old_position = 2
    left = 0
    right = 0
    cap = cv2.VideoCapture("sample.mp4")
    while cv2.waitKey(1) != 27:
        ret, image = cap.read()
        if not ret:
            break
        mask = cv2.inRange(image, (80, 80, 80), (255, 255, 255))
        ret, thresh = cv2.threshold(mask, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        a = x + (w // 2)
        b = y + (h // 2)
        fly = cv2.imread("fly64.png")
        fly = cv2.resize(fly, (64,64))
        for i in range(64):
            for j in range(64):
                dx = (a - 32 + j)
                if dx < 0:
                    dx = 0
                if dx > image.shape[1] - 1:
                    dx = image.shape[1] - 1
                dy = (b - 32 + i)
                if dy < 0:
                    dy = 0
                if dy > image.shape[0] - 1:
                    dy = image.shape[0] - 1
                image[dy][dx] = fly[j][i]
        cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



task1()
task2()
task3()
additional_task()