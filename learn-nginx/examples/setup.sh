echo "127.0.0.1 mysite" | sudo tee -a /etc/hosts
sudo nginx

# Setup and start app-one
cd app-one

# Install app-one as a daemon and start it
cp app-one.service /etc/systemd/system/
systemctl start app-one

# Configure nginx to serve app-one
echo "127.0.0.1 appone.mysite" | sudo tee -a /etc/hosts
sudo cp app-one.conf /etc/nginx/conf.d
sudo nginx -t
sudo nginx -s reload

cd ..

# Setup and start app-one
cd app-two

# Install app-one as a daemon and start it
cp app-two.service /etc/systemd/system/
systemctl start app-two

# Configure nginx to serve app-one
echo "127.0.0.1 apptwo.mysite" | sudo tee -a /etc/hosts
sudo cp app-two.conf /etc/nginx/conf.d
sudo nginx -t
sudo nginx -s reload

cd ..
