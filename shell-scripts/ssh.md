## SSH root login 
Edit this file: `sudo nano /etc/ssh/sshd_config`
```bash
sudo nano /etc/ssh/sshd_config
```
Find: `PermitRootLogin without-password`
```bash
PermitRootLogin yes 
```
Restart service
```bash
sudo service ssh restart 
```
Set `root` password
```bash
sudo passwd root
```