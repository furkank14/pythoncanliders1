import cv2

img = cv2.imread(r"images\1.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Resim",img)
cv2.imshow("Resi2m",gri)
cv2.waitKey(0)
cv2.destroyAllWindows()