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


Also, We know that deep learning is mainly dependent on Data. Due to lack of Animal categories in COCO, very strong detection was not achieved. [Imagenet](http://www.image-net.org/) has Animal categories and we differentiate it with COCO, in the Image Classification section. The best strategy would be to form a huge dataset of animals only, this will help us classify the breeds and types as well.

We also tried YOLO on Thermal, Night Vision, IR and Normal Video Feeds and the differences were astonishing. Please check <b>1:00</b> of this [video](https://youtu.be/sCrg1bD2Lno) to get a gist.

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/ewd2.jpg">

Several frames of object localization and classification are being portrayed in the following frames.

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/thermal2.jpg">

<h2> ➋ Image Classification </h2>

Classifying images of wildlife and having a bounding box is essential for detection. Used both ResNet50 and VGG16, trained on [ImageNet](https://github.com/SKKSaikia/sih2k18/blob/master/Image/Imagenet-script.py) and [COCO](https://github.com/SKKSaikia/sih2k18/blob/master/Image/COCO-script.py) datasets. Since COCO is a dataset based on real life objects, animal classification is a bit hard and inaccurate. It is able to detect & bound the animal, but not correctly classify it. The COCO outputs are:
<img src="https://github.com/SKKSaikia/sih2k18/blob/master/img/comparison.jpg">

As we can see:

    1>

The second Output from Imagenet:

<img src="https://github.com/SKKSaikia/sih2k18/blob/master/Image/output/ResNet50.JPG">

As we can compare from both the COCO and ImageNet outputs,


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


