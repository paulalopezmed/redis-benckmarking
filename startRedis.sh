gcloud compute instances create redis --zone="europe-west1-c"
sleep 60s
SUT_IP="$(gcloud compute instances describe redis --zone='europe-west1-c' --format='get(networkInterfaces[0].accessConfigs[0].natIP)')"
echo "SUT IP is $SUT_IP"

#Redis launch with Docker and previous requiered installation  

 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt update'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt upgrade -y'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt-get install -y -q language-pack-de'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt install -y -q apt-transport-https ca-certificates curl software-properties-common'
 gcloud compute ssh redis --zone europe-west1-c -- 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo add-apt-repository --yes "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt install -y -q apt-transport-https ca-certificates curl software-properties-common'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt update'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt upgrade -y'
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo apt install -y -q docker-ce'
 echo "Previous requiered installation finished"
 gcloud compute ssh redis --zone europe-west1-c -- 'sudo docker run -p 6379:6379 --name redis -d --rm docker.io/redis'

echo "Container started on port 6379"