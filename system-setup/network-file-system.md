# Network File System
Server IP is: `SERVER_IP`

Client IP is: `CLIENT_IP`

## Server side
- Install NFS server
```bash
apt install nfs-kernel-server 
```
- Shared directory name: `NFS`
```bash
chmod -R 777 NFS/ 
```
- Configure
```bash
nano /etc/exports
```
```bash
/media/suvam/Storage/NFS `CLIENT_IP`(rw,sync,no_subtree_check)
```
- Restart service
```bash
systemctl restart nfs-kernel-server.service
```
- Check
```bash
exportfs -a
```
```bash
showmount -e
```

## Client side
-  Install
```bash
apt install nfs-kernel-server 
```
- Check
```bash
showmount -e `SERVER_IP`
```
- Mount volume
```bash
mount -t nfs `SERVER_IP`:/media/suvam/Storage/NFS/satnet-data /home/suvam/NFS
```
- Umount volume
```bash
umount -f -l /home/suvam/NFS
```
