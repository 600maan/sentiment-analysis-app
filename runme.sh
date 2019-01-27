  #!/bin/bash
 
echo "Install Python 3.7 and required dependencies"
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3.7
sudo apt install -y python3-pip
sudo pip3 install -r requirements.txt --user 
 
echo "Start Python Application"
sudo pip3 install sklearn --user
sudo python3 -m nltk.downloader all
sudo python3 manage.py runserver 0.0.0.0:80
 