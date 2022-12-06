# CS5914-final-project

## Reference paper  
Disrupting Deepfakes: Adversarial Attacks Against Conditional Image Translation Networks and Facial Manipulation Systems  
https://arxiv.org/pdf/2003.01279.pdf  

## Group 3  
Name: Ting-Chih Chen and Xiao Guo  

## Task-1 Break down the defender  

```bash
├── Task-1
    ├── Dataset
        ├── CelebA-100.zip
        └── target_images.zip
    ├── GHOST
        ├── Readme.md
        └── Task1_GHOST.ipynb
    ├── StyleGAN-NADA
        ├── stylegan_nada.ipynb
        ├── resultsA.zip
        ├── resultsK.zip
        └── resultsO.zip
    ├── fewshot-face-translation-GAN
        ├── Results
            ├── Results_ariana.zip
            ├── Results_kobe.zip
            └── Results_obama.zip
        ├── Task1_Online_tool.ipynb
    ├── Evaluation.py
    └── Results - Task1.csv
```

Method-1: fewshot-face-translation-GAN  
Method-2: GHOST  
Method-3: StyleGAN-NADA  

CelebA-100.zip includes about 100 source images from CelebA and 100 perturbation images made from starGAN with imperceptible perturbations.  
target_images.zip includes three target images(Kobe, Obama, and Ariana). We use these target images to do deepfake.  


### Results  
| GANs | MSE | SSIM | PSNR|
| :---: | :---: | :---: | :---: |
| fewshot-face-translation-GAN | 57.684 | 0.951 | 32.295 |  
| GHOST | 0.737 | 0.998 | 50.396 |  
| StyleGAN-NADA | 247.152 | 0.777 | 25.259 |  
| StyleGAN-Baseline | 226.91 | 0.799 | 26.611 |  

## Task-2 Reverse the perturbation images to source images  
Method-1: auto-encoder  
Method-2: Image restoration  

### Results  
