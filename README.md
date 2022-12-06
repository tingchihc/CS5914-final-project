# CS5914-final-project

## Reference paper  
Disrupting Deepfakes: Adversarial Attacks Against Conditional Image Translation Networks and Facial Manipulation Systems  
https://arxiv.org/pdf/2003.01279.pdf  

## Group 3  
Name: Ting-Chih Chen and Xiao Guo  

## Task-1 Test the transferability to other DeepFake models 

```bash
├── Task-1
    ├── Dataset
        ├── Readme.md
        ├── CelebA-100.zip
        └── target_images.zip
    ├── GHOST
        ├── Readme.md
        └── Task1_GHOST.ipynb
    ├── StyleGAN-NADA
        ├── stylegan_nada.ipynb
        ├── Readme.md
        ├── resultsA.zip
        ├── resultsK.zip
        └── resultsO.zip
    ├── fewshot-face-translation-GAN
        ├── Results
            ├── Results_ariana.zip
            ├── Results_kobe.zip
            └── Results_obama.zip
        ├── Task1_Online_tool.ipynb
        └── Readme.md
    ├── Evaluation.py
    └── Results - Task1.csv

```

Method-1: fewshot-face-translation-GAN  
Method-2: GHOST  
Method-3: StyleGAN-NADA   


### Results  
| GANs | MSE | SSIM | PSNR|
| :---: | :---: | :---: | :---: |
| fewshot-face-translation-GAN | 57.684 | 0.951 | 32.295 |  
| GHOST | 0.737 | 0.998 | 50.396 |  
| StyleGAN-NADA | 247.152 | 0.777 | 25.259 |  
| StyleGAN-Baseline | 226.91 | 0.799 | 26.611 |  

## Task-2 Removing the perturbation in the images
```bash
├── Task-2
    ├──Autoencoder.ipynb 
    ├──Restormer.ipynb
    └──Task2DataSet.zip

### Results  
