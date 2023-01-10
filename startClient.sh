gcloud compute instances create client --zone="europe-west1-c"
sleep 60s
SUT_IP="$(gcloud compute instances describe client --zone='europe-west1-c' --format='get(networkInterfaces[0].accessConfigs[0].natIP)')"
echo "SUT IP is $SUT_IP"

#Client locust launch with locustfile.py and previous requiered installation and requirement.txt  

 gcloud compute ssh client --zone europe-west1-c -- 'sudo apt update'
 gcloud compute ssh client --zone europe-west1-c -- 'sudo apt upgrade -y'
 gcloud compute ssh client --zone europe-west1-c -- 'sudo apt-get pip'
 gcloud compute ssh client --zone europe-west1-c -- 'sudo apt-get install pip'
 gcloud compute scp $(pwd)/requirements.txt client:~/requirements.txt --zone europe-west1-c
 gcloud compute scp $(pwd)/locustfile.py client:~/locustfile.py --zone europe-west1-c
 gcloud compute ssh client --zone europe-west1-c -- 'pip3 install locust'
 gcloud compute ssh client --zone europe-west1-c -- 'sudo pip install locust'
 gcloud compute ssh client --zone europe-west1-c -- 'sudo pip install redis'
 echo "Previous requiered installation and files"
 gcloud compute ssh client --zone europe-west1-c -- 'locust --users 10 --csv=benchmark-preload.csv'

echo "Locust launch in 6379"