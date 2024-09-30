# Personalized-Learning-Assistant
An Adaptive-RAG + Gemini 1.5Pro based learning Assistant developed while keeping in mind the engineering students who study one night before exam 😉  
Keep forgetting things? Not anymore...  
Just one step away from an assistant to answer what you forgot 🏃‍➡️🏃‍➡️🏃‍➡️  
# Prerequisites
1. Linux based Operating System (WSL would also work)
2. Docker
# Setup
### Clone this Repository  
``` linux/wsl
git clone https://github.com/RujhaanTaneja/Personalized-Learning-Assistant
```
### Files
Place all the semester's course content in the Data folder in the cloned Repository on your system.  
We recommend use of Pdf files, but it is compatible for all image-based files, PPTs, Word Documents, etc
### Go to this repo
``` linux/wsl
cd Personalized-Learning-Assistant
```

### Create a docker image
This may take a while to run. 
``` linux/wsl
docker build -t pla .
```
### Create a container
``` linux/wsl
docker run -it --name presonal-pla pla
```
# Ask Questions?  
Now, It will start to process the files you provided it, and soon it will prompt 'Enter a Question:'
### Congratulations! The setup is complete
Now, you can enjoy the capabilities of this Assistant on your fingertips...  
Just enter a Question and It will produce an Answer almost immediately  
After answering, It will again prompt for a question...  
You may ask another question or close the tab
# Inference 
Now, If you are willing to access the assistant again  
Just:
``` linux/WSL
docker start -i personal-pla
```
##Voila! Enjoy the way of new, efficient Learning
#Good Luck for Your exams
