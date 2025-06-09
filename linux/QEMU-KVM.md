# How to setup

### Check CPU virtualization support
```bash
lscpu | grep Virtualization
```

### Install virtual package `qemu-kvm`
```bash
sudo apt install qemu-kvm
```

### Install virtualization API `libvirt-daemon-system` and `libvirt-clients`
```bash
sudo apt install libvirt-daemon-system libvirt-clients
```

### Add user to KVM group
```bash
sudo adduser $USER kvm
```
Reboot and check user groups
```bash
groups
```

### Check KVM installation status
```bash
virsh list --all
```

### Install `virt-manager` for GUI
```bash
sudo apt install virt-manager
```



# Networking

List of virtual bridegs in the system using `bridge-utils`
```bash
sudo apt install bridge-utils
```
Bridge control (brctl) show the list of bridges
```bash
brctl show
```

### Create bridge network
Expose VMs to local network using virtual bridge and ethernet as slave
1. Network Manager Text User Interface
```bash
sudo nmtui
```
2. Edit a connection
3. Add
4. Bridge
5. Create
6. Default name `nm-bridge`
7. Add (slave)
8. Ethernet
9. Create
10. Back

Finally, delete `Wired connection 1`
1. Edit a connection
2. `Wired connection 1`
3. Delete
4. Delete
5. Quit



```bash
ifconfig
```
No IP address in `eno1` but `nm-bridge` have one IP address
```bash
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether c0:18:03:be:3b:06  txqueuelen 1000  (Ethernet)
        RX packets 21987059  bytes 11443963246 (11.4 GB)
        RX errors 0  dropped 41  overruns 0  frame 0
        TX packets 4301969  bytes 745947903 (745.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 19  memory 0x80900000-80920000 

nm-bridge: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.27.27.147  netmask 255.255.0.0  broadcast 172.27.255.255
        inet6 fe80::ef14:56b3:f17c:d028  prefixlen 64  scopeid 0x20<link>
        ether 4a:8d:a9:67:cf:7a  txqueuelen 1000  (Ethernet)
        RX packets 433411  bytes 1187614336 (1.1 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 137654  bytes 90977212 (90.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```
`eno1` is interface in `nm-bridge`
```bash
brctl show
```
Now VMs in bridge netowrk will get IP address form the local network (physical).