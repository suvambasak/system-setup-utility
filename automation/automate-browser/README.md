# Automate chrome browser

## Setup
### Chrome driver
https://chromedriver.chromium.org/downloads

```bash
unzip chromedriver_linux64.zip && sudo mv chromedriver /usr/bin/chromedriver && sudo chown root:root /usr/bin/chromedriver && sudo chmod +x /usr/bin/chromedriver && rm chromedriver_linux64.zip
```
### Install dependencies
```bash
sudo apt-get install xvfb python3-pip
```
```bash
pip3 install selenium pyvirtualdisplay
```

### login
```bash
python3 autologin.py
```


## Crontab
```bash
crontab -e
```

```bash
0 * * * * python3 /path_to_script/autologin.py 
```

