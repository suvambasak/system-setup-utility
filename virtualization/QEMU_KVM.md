### Chek CPU virtualization support
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