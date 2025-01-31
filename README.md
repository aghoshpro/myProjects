# Data Science Projects

## Local Environment Setup

### Using Python `venv` 🐍

- Go to location using `cmd` or `terminal`

  ```bash
  python -m venv myvenv
  ```

  ```sh
  # On Windows
  .\myvenv\Scripts\activate --OR-- source myvenv/bin/activate # On Linux or Mac
  ```

  ```sh
  pip install -r requirements.txt
  ```

### Using Docker 🐳

- Go to location using `cmd` or `terminal`

  ```sh
  cd env_docker
  ```

  ```sh
  docker compose -f docker-compose.yml up
  ```

- Put the desired notebook in the `notebook` directory along with the data in the `data` folder.

### Using Conda 🧶

- Open your favourite `terminal` or `cmd` to download the dependencies listed in `envALL.yml`

  ```sh
  conda env create -f envALL.yml
  ```

---

## 11. Sparkify - Detection of User Churn using PySpark

Forecasting churn or attrition rates presents a complex and prevalent challenge that data scientists and analysts frequently face in customer-oriented enterprises.
The capacity to adeptly handle extensive datasets using Spark is among the most sought-after competencies in the data domain.
Also to convey the findings of the project to company shareholder in a manner so they can understand.

- Check out the jupyter [notebook](https://github.com/aghoshpro/myProjects/tree/main/Data-Scientist-Nanodegree/Project%204%20-%20Sparkify)
- Check out [medium blogpost](https://medium.com/@aghoshpro/beat-the-churn-how-were-using-pyspark-ml-to-keep-the-music-streaming-2b202dca6aaa) to understand the project in detail.

## 10. Personalized Real Estate Agent

Envision yourself as a skilled developer at "Future Homes Realty," an innovative real estate firm. In an industry where personalisation is crucial for consumer satisfaction,
your company aims to transform client interactions with real estate listings. To create a novel application called `HomeMatch` that utilises large language models (LLMs) and vector databases to
convert conventional real estate listings into customised narratives that align with the distinct preferences and requirements of prospective purchasers.

- Check out the jupyter [notebook](https://github.com/aghoshpro/myProjects/blob/main/GenAI/Project%204%20-%20Real%20Estate%20Agent/HomeMatch.ipynb)

## 9. ChatBOT using Retrieval Augmented Generation (RAG)

Custom Chatbot project so that our fashion-focused chat interface can work with it. The information in this dataset carefully shows the complex changes that happen in modern fashion. It includes famous colour schemes, fabric choices, and other important fashion insights seen in 2023. This dataset fits perfectly intending to make it easier to create a complex chatbot that can meet the specific needs of fashion fans and people who work in the industry.

- Check out the jupyter [notebook](https://github.com/aghoshpro/myProjects/blob/main/GenAI/Project%202%20-%20RAG%20ChatBOT/project.ipynb)

## 8. Landmark Classification (using CNN) & Tagging for Social Media

- Check out the [app](https://github.com/aghoshpro/myProjects/tree/main/Deep-Learning-NanoDegree/Project%2002%20-%20Landmark%20Classification%20%26%20Tagging%20for%20Social%20Media#landmark-classification)

- Check out the jupyter [notebook](https://github.com/aghoshpro/myProjects/tree/main/Deep-Learning-NanoDegree/Project%2002%20-%20Landmark%20Classification%20%26%20Tagging%20for%20Social%20Media#landmark-classification)

## 7. Classification of Handwritten Digit using MNIST Data

The task is to classify a given image of a handwritten digit into one of 10 classes representing integer values from 0 to 9, inclusively.

The [MNIST](https://en.wikipedia.org/wiki/MNIST_database) is a standard dataset used in computer vision and deep learning. The MNIST acronym stands for the Modified National Institute of Standards and Technology dataset. It has 60,000 small square 28×28 pixel grayscale images of handwritten single digits between 0 and 9.

- Check out the jupyter [notebook](https://github.com/aghoshpro/myProjects/blob/main/Deep-Learning-NanoDegree/Project%2001%20-%20MNIST%20Handwritten%20Digits%20Classifier%20with%20PyTorch/MNIST_Handwritten_Digits-STARTER.ipynb)

## 6. Disaster Response System

I analyzed disaster data to build a model for an API that classifies disaster messages by applying my data engineering skills. I have created a ML pipeline to categorize real messages that were sent during disaster events so that the messages could be sent to an appropriate disaster relief agency. The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data.

- Check out the [app](https://github.com/aghoshpro/myProjects/tree/main/Data-Scientist-Nanodegree/Project%202%20-%20Disaster%20Response%20App#project-2---disaster-response-pipeline-project)

## 5. Real World Object Detection using COCO dataset

Detecting objects with **65% confidence** using pre-trained `MobileNet-SSD v3` model and **183 labels** or **classes** from `COCO 2017` dataset. User can also use webcam to detect objects around their surroundings by running `objectDetectionWebCam.py`

- Check out the [project](https://github.com/aghoshpro/myProjects/tree/main/Object%20Detection%20CV#object-detection-using-opencv)

<img src="./Object Detection CV/FIFA.gif">

## 4. Sip & Script

I ran an exploratory data analysis utilizing a [Wine Reviews Dataset](https://www.kaggle.com/datasets/zynicide/wine-reviews) from Kaggle, which contained roughly 130k Wine Enthusiast reviews. I took this project as an opportunity to analyse the data and explain my results through a [medium blog](https://medium.com/@aghoshpro/sip-script-a-data-driven-journey-through-the-world-of-wine-d9d05d6dcf4e) post that provides insight into the questions posed.

- Check out the jupyter [notebook](https://github.com/aghoshpro/myProjects/blob/main/Data-Scientist-Nanodegree/Project%201%20-%20WineTestingBlog/Sip%20%26%20Script.ipynb)

## 3. Multi-Class Dog Breed Classification

The aim is to create a classifier capable of predicting a dog's breed from a photo.
In a real world scenario when someone takes a photo of a dog and wants to know what breed of dog it is using this model.
The [dataset](https://www.kaggle.com/c/dog-breed-identification) contains 20000+ images of dogs of 120 breeds (12- classes)

- Check out the jupyter [notebook](https://colab.research.google.com/drive/1WdmR5UmvmP3QMo9WyuSXOQLqC0MHSuzJ)

## 2. Multi Class Image Classifier

Building a neural network using PyTorch to evaluate the CIFAR-10 dataset. It takes an input image and predicts the class out of 10 classes from CIFAR with accuracy **52%**.

- Data - [CIFAR10](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)

- Check out the jupyter [notebook](https://github.com/aghoshpro/myProjects/blob/main/Deep-Learning-NanoDegree/CIFAR-10_Image_Classifier-STARTER.ipynb)

## 1. Heart Disease Prediction using Regression

**Question. Can the presence of heart disease in the patient be predicted based on their clinical parameters?**

The [dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) contains 76 attributes, but all published experiments refer to using a subset of 14 of them. It is part of Cleveland database that has been used by ML researchers to this date and originated from UCI Machine Learning [Repository](https://archive.ics.uci.edu/dataset/45/heart+disease).

---

<!--
## Pytorch Installation (with GPU)

### 0. Guide to local setup using GPU: https://pytorch.org/get-started/locally/

### 1. Nvidia CUDA Toolkit Setup

#### 1.1 Open `cmd` to check if the machine has a GPU-CUDA access

```sh
C:\>nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Tue_May__3_19:00:59_Pacific_Daylight_Time_2022
Cuda compilation tools, release 11.7, V11.7.64
Build cuda_11.7.r11.7/compiler.31294372_0
```

#### 1.2. Else follow the following steps

- Go to [Cuda Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) and download the toolkit version (11.7) supported by Pytorch.

- Install the Cuda Toolkit and after installation run the following `nvcc --version` in CMD to check CUDA version.

### 2. Installing PyTorch

#### 2.1. Create a virtul environment in local drive

```sh
(base) D:\workspace_Data_Science>conda create -n env_torch
```

```sh
(base) D:\workspace_Data_Science>conda activate env_torch
```

#### 2.2 Install PyTorch according to [Guide](https://pytorch.org/get-started/locally/)

```sh
(env_torch) D:\workspace_Data_Science>conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

```sh
## Package Plan ##

  environment location: C:\Anaconda_2021\envs\env_torch

  added / updated specs:
    - pytorch
    - pytorch-cuda=11.7
    - torchaudio
    - torchvision


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    brotlipy-0.7.0             |py310h2bbff1b_1002         335 KB
    ca-certificates-2023.01.10 |       haa95532_0         121 KB
    certifi-2022.12.7          |  py310haa95532_0         149 KB
    cffi-1.15.1                |  py310h2bbff1b_3         239 KB
    cryptography-39.0.1        |  py310h21b164f_0         1.0 MB
    cuda-demo-suite-12.1.55    |                0         4.7 MB  nvidia
    cuda-documentation-12.1.55 |                0          89 KB  nvidia
    cuda-nsight-compute-12.1.0 |                0           1 KB  nvidia
    cuda-nvdisasm-12.1.55      |                0        48.0 MB  nvidia
    cuda-nvprof-12.1.55        |                0         1.6 MB  nvidia
    cuda-nvvp-12.1.55          |                0       113.6 MB  nvidia
    cuda-sanitizer-api-12.1.55 |                0        12.9 MB  nvidia
    giflib-5.2.1               |       h8cc25b3_3          88 KB
    idna-3.4                   |  py310haa95532_0          97 KB
    jpeg-9e                    |       h2bbff1b_1         320 KB
    libcurand-10.3.2.56        |                0           3 KB  nvidia
    libcurand-dev-10.3.2.56    |                0        50.0 MB  nvidia
    .
    .
    . and many more
```

#### 2.3 Check if pytorch installed successfully ???

```sh
(env_torch) D:\workspace_Data_Science>python
Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>>
>>>
>>> print(torch.rand(2,4))
tensor([[0.1220, 0.2692, 0.8196, 0.2800],
        [0.3619, 0.8364, 0.9870, 0.7860]])
>>> torch.cuda.is_available()
True
>>> torch.cuda.device_count()
1
>>> torch.cuda.get_device_name()
'NVIDIA GeForce RTX 2060'
```

#### 2.5 Install required pkgs

```
(env_torch) D:\workspace_Data_Science>conda install pandas matplotlib seaborn scikit-learn
``` -->

## Additional Data

- [Arthropod Taxonomy Orders Object Detection Dataset](https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset): Invertebrate animal (arthropod) images annotated for object detection

- [Create Object Detection Video](https://www.kaggle.com/code/mistag/create-object-detection-video): In this notebook we will run object detection on a video, frame by frame, using a model trained in another notebook. Then we will render a new video with the detections.
