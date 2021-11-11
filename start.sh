if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Rzeeo/Mine.git /Mine
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Mine
fi
cd /EVA-3.0
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
