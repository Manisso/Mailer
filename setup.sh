#!/bin/bash
clear
pip install mechanize
pip install requests
pip install os

clear

rm -R "/usr/share/doc/Mailer"


sudo sudo git clone https://github.com/Manisso/Mailer.git /usr/share/doc/Mailer;

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
