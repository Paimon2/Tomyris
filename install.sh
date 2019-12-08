if [[ $EUID -ne 0 ]]; then
   echo "This script must be run with root permissions." 
   exit 1
fi

echo -e "Installing Tomyris as a systemd service. The process will begin in 5 seconds.\nCTRL+C to cancel."
sleep 5
echo "Cloning Tomyris into /opt (1/6)..."
cd /opt
git clone https://github.com/UltraFuture7000/Tomyris tomyris
echo "Installing requirements (2/6)..."
pip install -r /opt/tomyris/requirements.txt
echo "Installing systemd service (3/6)..."
cp /opt/tomyris/tomyris.service /etc/systemd/system
chmod 644 /etc/systemd/system/tomyris.service
echo "Setting up systemd service (4/6)..."

read -p "Automatically start Tomyris on boot (y/n)? " persistentstart
if [[ $persistentstart =~ ^(yes|y| ) ]] || [[ -z $persistentstart ]]; then
  systemctl enable tomyris;
  echo "Tomyris will be automatically started at boot."
fi

echo "Installing tomyrisctl (5/6)..."
cp /opt/tomyris/tomyrisctl.py /usr/bin
mv /usr/bin/tomyrisctl.py /usr/bin/tomyrisctl
chmod a+x /usr/bin/tomyrisctl
echo "Configuring Tomyris (6/6)..."
# configparser will be used to read these files


read -p "What's the host of your database? " dbhost
read -p "What's the port of your database (if unsure, type 3306)? " dbport
read -p "What user should we use to access your database? " dbuser
read -p "What's the password of that user? " dbpassword
read -p "And finally, what's the name of your database? " dbname

rm -f /opt/tomyris/config.txt
echo -e "[DATABASE]\n" >> /opt/tomyris/config.txt
echo -e "Host = $dbhost" >> /opt/tomyris/config.txt
echo -e "Port = $dbport" >> /opt/tomyris/config.txt
echo -e "User = $dbuser" >> /opt/tomyris/config.txt
echo -e "Password = $dbpassword" >> /opt/tomyris/config.txt
echo -e "Name = $dbname" >> /opt/tomyris/config.txt


read -p "Start Tomyris now (y/n)? " persistentstart
if [[ $persistentstart =~ ^(yes|y| ) ]] || [[ -z $persistentstart ]]; then
  systemctl start tomyris;
  echo "Tomyris has been started."
fi

echo "Tomyris has been installed!"
echo "View https://github.com/UltraFuture7000/Tomyris/blob/master/README.md for help."