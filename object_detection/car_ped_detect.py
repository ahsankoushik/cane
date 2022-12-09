import cv2
# import imutils

# flags
objects = {
    'cars' : [],
    'pedestrian' : []
}
x_dic = {
    1 : 'left',
    2 : 'center',
    3 : 'right'
}
y_dic = {
    1 : 'bottom',
    2 : 'center',
    3 : 'top'
}

short ={
    'left' : {'car':0,'pedestrian':0},
    'center' : {'car':0,'pedestrian':0},
    'right' : {'car':0,'pedestrian':0}

}

def image_description(img_url:str):

    # Initializing the HOG person
    # detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    car_cascade = cv2.CascadeClassifier('object_detection/models/cars.xml')

    image = cv2.imread(img_url)
    (height, width) = image.shape[:2]
    # print(height,width)


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1)

    for (x, y, w, h) in regions :
        l =[]
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
        # print(x+w//2,y+h//2)
        cv2.circle(image,(x+w//2,y+h//2),3,(0,255,0),1)
        for i in range(1,4):
            cv2.line(image,((width//3)*i,0),((width//3)*i,height),(0,0,0),1)
            cv2.line(image,(0,(height//3)*i),(width,(height//3)*i),(0,0,0),1)
            if ((width//3)*(i-1)) < (x+w//2) < ((width//3)*i):
                l.append(x_dic[i])
                short[x_dic[i]]['pedestrian'] += 1

                # print(i,,((width//3)*(x-1)), (x+w//2) ,((width//3)*i))
            if ((width//3)*(i-1)) < (y+h//2) < ((height//3)*i):
                l.append(y_dic[i])
        objects['pedestrian'].append(l)


        
    c = 0
    for (x,y,w,h) in cars:
        l=[]
        # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.circle(image,(x+w//2,y+h//2),3,(255,0,0),1)

        for i in range(1,4):
            cv2.line(image,((width//3)*i,0),((width//3)*i,height),(0,0,0),2)
            if ((width//3)*(i-1)) < (x+w//2) < ((width//3)*i):
                l.append(x_dic[i])
                short[x_dic[i]]['car'] += 1

                # print(i,,((width//3)*(x-1)), (x+w//2) ,((width//3)*i))
            if ((height//3)*(i-1)) < (y+h//2) < ((height//3)*i):
                l.append(y_dic[i])
            # if c in [3,5]:
            #     # print(((width//3)*(i-1)) , (y+h//2) , ((height//3)*i))
        objects['cars'].append(l)
        c += 1
        # cv2.putText(image,str(l)+str(c),((x+w//2)+3,(y+h//2)), cv2.FONT_HERSHEY_SIMPLEX,.3,(0,0,255))

    # print(objects)
    car_str = f'There are total {len(objects["cars"])} cars and {len(objects)} pedestrians.'
    for key,val in short.items():
        f = 1
        if val['car'] > 0:
            if f: 
                car_str += f' On your {key}'
                f = 0
            car_str += f' there are {val["car"]} cars'
        if val['pedestrian'] > 0:
            if f: 
                car_str += f' On your {key}'
                f = 0
            car_str += f'and {val["pedestrian"]} pedestrians'

    return car_str

# Showing the output Image
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# cv2.destroyAllWindows()


if __name__ == '__main__':
    print(image_description('car+ped.jpg'))