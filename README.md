# Smart India Hackathon 2018

+ Problem statement: [A real time recording and monitoring of human activities and animal movements in Protected Areas](https://innovate.mygov.in/sih_ps/a-real-time-recording-and-monitoring-of-human-activities-and-animal-movements-in-protected-areas/)

<img src = "https://github.com/SKKSaikia/sih2k18/blob/master/img/sih.jpg">

Team – <b>Dark_Forest</b>

KPIT: Innovation Award Winner, Smart India Hackathon, 2018
Ministry of Environment, Forest and Climate Change

<b>Team Members:</b>

Amartya Ranjan Saikia (<b>TL</b>), Joy Dutta, Pulkit Singh, Sandeep Talukdar, Priyangshu Yogi, Tahera Aktar Laskar;
Assam Engineering College, Guwahati, India

<b>Team Mentors:</b>
Lakhya Jyoti Bora, Biju Pegu;
Gratia Technology Pvt. Ltd.




# ABSTRACT
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/overview.JPG">

We provided an end to end solution 


# END-TO-END

# DEEP LEARNING

<h2> ➊ Object Detection </h2>

    1. Real Time
    2. Video Feed
    
[YOLOv2](https://pjreddie.com/darknet/yolo/) trained on [COCO](http://cocodataset.org) was used for Object detection. [Darkflow](https://github.com/thtrieu/darkflow) which is a Tensorflow variant of [Darknet](https://github.com/pjreddie/darknet) was used to process the frames. Darknet is an open source neural network framework written in C and CUDA. 

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/yolo.JPG">

The output video in the Hackathon are: [Webcam](https://youtu.be/SJxoIHBeOB0) , [Mobile Camera](https://youtu.be/qkzmv4ny7VM)

Several images of Guns, Poachers, Rangers were scraped from the internet and YOLOv2 was trained from scratch to detect the following object classes in the frames. Due to lack of data and time in the hackathon, high accuracy and confidence was not achieved.


Wildlife Video Feed was fed to the layers of YOLO and animals / humans were tracked with high confidence in the wildlife. Some of the frames are :


Also, We know that deep learning is mainly dependent on Data. Due to lack of Animal categories in COCO, very strong detection was not achieved. [Imagenet](http://www.image-net.org/) has Animal categories and we differentiate it with COCO, in the Image Classification section. The best strategy would be to form a huge dataset of animals only, this will help us classify the breeds and types as well.

We also tried YOLO on Thermal, Night Vision, IR and Normal Video Feeds and the differences were astonishing. Please check <b>1:00</b> of this [video](https://youtu.be/sCrg1bD2Lno) to get a gist.


