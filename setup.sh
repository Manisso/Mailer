pip install mechanize
pip install requests
pip install os

clear

if [ -d "/usr/share/doc/Mailer" ] ;
then
rm -R "/usr/share/doc/Mailer"
else
 exit
fi

sudo cd /usr/share/doc/
sudo git clone https://github.com/Manisso/Mailer.git

echo "#!/bin/bash 
 python /usr/share/doc/Mailer/inbox.py" '${1+"$@"}' > inbox;
 chmod +x inbox;
 sudo cp inbox /usr/bin/;
rm inbox;

if [ -d "/usr/share/doc/Mailer" ] ;
then

echo "[✔] ✔✔✔  All is done!! You can execute tool by typing inbox !   ✔✔✔ [✔]"; 

else
  echo "[✘] Installation faid![✘] ";
  exit
fi

xterm inbox

exit
