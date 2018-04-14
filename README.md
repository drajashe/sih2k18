# Smart India Hackathon 2018

+ Problem statement: [A real time recording and monitoring of human activities and animal movements in Protected Areas](https://innovate.mygov.in/sih_ps/a-real-time-recording-and-monitoring-of-human-activities-and-animal-movements-in-protected-areas/)

<img src = "https://github.com/SKKSaikia/sih2k18/blob/master/img/sih.jpg">

Team – <b>Dark_Forest</b>

KPIT: Innovation Award Winner, Smart India Hackathon, 2018

Ministry : Ministry of Environment, Forest and Climate Change

<b>Team Members:</b>

Amartya Ranjan Saikia (<b>TL</b>), Joy Dutta, Pulkit Singh, Sandeep Talukdar, Priyangshu Yogi, Tahera Aktar Laskar;
Assam Engineering College, Guwahati, India

<b>Team Mentors:</b>

Lakhya Jyoti Bora, Biju Pegu;
Gratia Technology Pvt. Ltd.




# ABSTRACT
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/overview.JPG">

We provided an affordable, scalable and state of the art end to end solution for tackling poaching and tracking animals/humans in protected areas.The whole idea comprises of three parts:

    1. Android
    2. Web
    3. Intelligence (Deep Learning)
    
The idea is that, the rangers will have a light weight android app with them and they will be able to monitor/report activities in wildlife. The android app ui has a map, showing real time location of all the rangers in black and displays some other features like temperature, humidity etc. The ui also has a red button, so that the rangers can press at any time in case they detect/suspect any poaching activity. As soon as they press the red button, the longitude and latitude of the ranger pressing the button will be sent to the web server and the server will update each and every rangers app showing shortest path from each and every rangers location to thr location in DANGER(in RED Color). The shortest path will be found just like that of UBER. As you go through #Image Processing part of Deep Lerning, more information on finding the shortest path is noted down. The whole Idea is large and involved many part, includeing Raspberry Pi, Camera configuration etc to meet the ends. The strategy to install them, connect them with sensors, monitoring station and the rangers in unique to us.

I personally worked on Deep Learning and I am giving you some of the insights into our project. The Android and Web parts are unique and are not discussed here.

# DEEP LEARNING
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/deep.jpg">

The Deep Learning section comprises of Object Detection, Image Classification, Audio Classification, Image Processing and Predictive Analysis. Each of the section are written down with detailed description.

<h2> ➊ Object Detection </h2>

    1. Real Time
    2. Video Feed
    
[YOLOv2](https://pjreddie.com/darknet/yolo/) trained on [COCO](http://cocodataset.org) was used for Object detection. [Darkflow](https://github.com/thtrieu/darkflow) which is a Tensorflow variant of [Darknet](https://github.com/pjreddie/darknet) was used to process the frames. Darknet is an open source neural network framework written in C and CUDA. 

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/yolo.JPG">

The output video in the Hackathon are: [Webcam](https://youtu.be/SJxoIHBeOB0) , [Mobile Camera](https://youtu.be/qkzmv4ny7VM)

Several images of Guns, Poachers, Rangers were scraped from the internet and YOLOv2 was trained from scratch to detect the following object classes in the frames. Due to lack of data and time in the hackathon, high accuracy and confidence was not achieved.

Wildlife Video Feed was fed to the layers of YOLO and animals / humans were tracked with high confidence in the wildlife. Some of the frames are :

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/wildd.jpg">

Also, We know that deep learning is mainly dependent on Data. Due to lack of Animal categories in COCO, very strong detection was not achieved. [Imagenet](http://www.image-net.org/) has Animal categories and we differentiate it with COCO, in the Image Classification section. The best strategy would be to form a huge dataset of animals only, this will help us classify the breeds and types as well.

We also tried YOLO on Thermal, Night Vision, IR and Normal Video Feeds and the differences were astonishing. Please check <b>1:00</b> of this [video](https://youtu.be/sCrg1bD2Lno) to get a gist.

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/ewd2.jpg">

Several frames of object localization and classification are being portrayed in the following frames.

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/thermal2.jpg">

The bounding box frame classes are sent to the servers in real time in .json and .csv format. This is text sent to servers for classes detected.

<h2> ➋ Image Classification </h2>

Classifying images of wildlife and having a bounding box is essential for detection. Used both ResNet50 and VGG16, trained on [ImageNet](https://github.com/SKKSaikia/sih2k18/blob/master/Image/Imagenet-script.py) and [COCO](https://github.com/SKKSaikia/sih2k18/blob/master/Image/COCO-script.py) datasets. Since COCO is a dataset based on real life objects, animal classification is a bit hard and inaccurate. It is able to detect & bound the animal, but not correctly classify it. The COCO outputs are:
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/comparison.jpg">

As we can see:

    1> Correct Bounding Box, Incorrect Classification
    2> Correct Bounding Box, Correct Classification
    3> Correct Bounding Box, Incorrect Classification though image has camouflage
    4> Correct Bounding Box, Correct Classification

The second Output from Imagenet:

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/Image/output/ResNet50.JPG">

The ImageNet classification is more accurate for animals. Its classification output classes were different types of Tigers, or Elephants, but for COCO, the classifier was confused between a Tiger and a Bear for an image of Cheetah.
As we can compare from both the COCO and ImageNet outputs, we can conclude that for more accuracy, we need a dataset comprising of  only animals.

<h2> ➌ Audio Classification </h2>

With Sensors in jungles we intended to classify audio to track and detect animals. We know that sound waves are frequency spectrums and each animal's sound has different range of frequencies. Or in other terms each animal has different frequency image, so these can be learned with the help of a Convolutional Neural network (CNN). The [ESC-50](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YDEPUT) dataset from Harvard is a collection of environmental sounds and would serve the purpose for demonstration. A huge audio dataset of animals will be required for real life implementation. Google AI has a similar experiment and works on similar concepts - [BIRD SOUNDS](https://experiments.withgoogle.com/ai/bird-sounds/view/). The difference in frequencies of CAT vs DOG can be viewed here:
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/sound.jpg">
Here is the Sample [output](https://youtu.be/7nNgFzmIUsA).

<h2> ➍ Image Processing </h2>

Image processing algorithms to find roads and paths within jungles. We approached this in two ways:

    1) Image Processing
    2) GPS Tracking
    
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/satellite/img/sat_1.jpg">

Image Processing Algorithms inspired from [DSTL Satellite Imagery feature Detection](https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection) and some own algorithms, were accounted to find paths within jungles, so that we can find the realistic shortest paths between the ranger and the danger/poacher location. Image processing can only account for paths which are visible from satellite, but what about the tunnels and hidden from above paths in jungles.
We thought of tackling this by tracking the GPS locations of the rangers for a month or so, and asking them to patrol the sanctuary via tunnels and shortest hidden paths. That way, we track the GPS locations over the map and find the shortest paths within jungles.

<h2> ➎ Predictive Analysis </h2>
Machine Learning is learning from data right ? We can find patterns within data. In our case, we can collect data from past field study reports, journals/articles on the wildlife sanctuary/ National park or study reports by rangers/ngos etc. With this huge amount of data, we analyze them and predict some of the features. 

Made a dummy data report of poaching - [[data.csv](https://github.com/SKKSaikia/sih2k18/blob/master/pred/kaz_train.csv)] and found the following outcomes via graphs.
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/pred/graph.jpg">

# Conclusion

Thus we provided a low cost, state of the art solution, which can be implemented in the existing infrastructure of the wildlife sanctuaries / national parks. Thus integrating the hardware and software stacks we get a complete solution.


