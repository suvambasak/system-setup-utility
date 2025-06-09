# Secure Shell Setup

## Setup
### Install SSH server
```bash
sudo apt install openssh-server
```

### Generate SSH key pair
```bash
ssh-keygen
```

### Copy public key
```bash
ssh-copy-id username@remotehost
```

### SSH login
```bash
ssh username@remotehost
```

## Enable SSH root login
- Login, and edit this file
```bash
sudo nano /etc/ssh/sshd_config
```
- Find this line: `PermitRootLogin without-password` change to
```bash
PermitRootLogin yes
```
- Restart the service
```bash
sudo service ssh restart
```
- Set root password
```bash
sudo passwd root
```

## Create alias
- Create file: `.ssh/config`
- Add details
```bash
Host workstation
  HostName IP_ADDR_1
  User suvam
Host my-system
  HostName IP_ADDR_2
  User suvam
```