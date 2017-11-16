pip install mechanize
pip install requests
pip install os

if [ -d "/usr/share/doc/fsociety" ] ;
then
rm -R "/usr/share/doc/fsociety"
else
 exit
fi
fi

cd /usr/share/doc/
git clone https://github.com/Manisso/Mailer.git

echo "#!/bin/bash 
 python /usr/share/doc/Mailer/inbox.py" '${1+"$@"}' > inbox;
 chmod +x inbox;
 sudo cp inbox /usr/bin/;
rm inbox;

if [ -d "/usr/share/doc/fsociety" ] ;
then

echo "[✔] ✔✔✔  All is done!! You can execute tool by typing inbox !   ✔✔✔ [✔]"; 

else
  echo "[✘] Installation faid![✘] ";
  exit
fi

xterm inbox

exit
