# Clean up app one
systemctl stop app-one
rm /etc/systemd/system/app-one.service
systemctl daemon-reload
sudo sed -i 's/^127.0.0.1\s*appone\.mysite$//' /etc/hosts
sudo rm /etc/nginx/conf.d/app-one.conf
sudo nginx -t

# Clean up app two
systemctl stop app-two
rm /etc/systemd/system/app-two.service
systemctl daemon-reload
sudo sed -i 's/^127.0.0.1\s*apptwo\.mysite$//' /etc/hosts
sudo rm /etc/nginx/conf.d/app-two.conf
sudo nginx -t


sudo sed -i 's/^127.0.0.1\s*mysite$//' /etc/hosts
sudo nginx -s stop
