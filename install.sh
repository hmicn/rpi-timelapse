sudo apt install h5py
sudo apt-get install python3-h5py
sudo apt install libopenjp2-7
sudo apt install ffmpeg
sudo apt-get install libatlas-base-dev
pip install opencv-python-headless

sudo apt install apache2
sudo apt install php php-mbstring

sudo chmod -R 777 /var/www/html/
mkdir /var/www/html/images
mkdir /var/www/html/logs
sudo chmod -R 777 /var/www/html/

echo '* * * * * python take.py >> /var/www/html/logs/log.txt' > crontab.txt && crontab crontab.txt