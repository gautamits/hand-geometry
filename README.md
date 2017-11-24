###Recognise person by his hand shape and geometry
#####obtain hand image
![](documents/images/IMG_20161220_013140.jpg)
#####get binary image
![](documents/images/binary.png)
#####Get contour with centroid
![](documents/images/contour.png)
#####Extract convex hull of contour
![](documents/images/hull.png)
#####Extract valleys by convexity defects
![](documents/images/valleys.png)
#####Extract peaks as intersection of convex hull and cotour above centroid
![](documents/images/peaks.png)
#####Extract knuckles as midpoint between valleys
![](documents/images/knuckles.png)
#####Obtain seven lines as shown below
![](documents/images/lines.png)
#####Normalize them and store as feature vecor



