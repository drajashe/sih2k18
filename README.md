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



We trained several parts
