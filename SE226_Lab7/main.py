
import urllib.request
import cv2 as cv2
import numpy as np

url = "https://phantom-marca.unidadeditorial.es/9adff0247d936694d269507386084447/resize/828/f/webp/assets/multimedia" \
      "/imagenes/2022/05/19/16529335233738.jpg"
url_response = urllib.request.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, -1)

blue, green, red = cv2.split(img)
zero = np.zeros(blue.shape, np.uint8)
blue = cv2.merge((blue, zero, zero))
green = cv2.merge((zero, green, zero))
red = cv2.merge((zero, zero, red))
cv2.imshow("Doncic", img)
cv2.waitKey(0)
cv2.imshow("Blue Doncic", blue)
cv2.imshow("Green Doncic", green)
cv2.imshow("Red Doncic", red)
cv2.waitKey(0)
cv2.merge((cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY), zero, zero))
cv2.imshow("Psychological Breakdown Doncic", cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY))
cv2.waitKey(0)
cv2.destroyAllWindows()
