# utility

#### Create a video from frames (png)
```bash
ffmpeg -framerate 3 -pattern_type glob -i '/media/suvam/Storage/LEO-NET/toffset_0/*.png' -c:v libx264 -pix_fmt yuv420p output.mp4
```


### Open TimeShift in remote desktop (xrdp)
```bash
sudo /bin/bash -c "export XAUTHORITY=\"${HOME}/.Xauthority\" && timeshift-gtk"
```


### Available space device wise
```bash
df -h
```

### Directory size
```bash
du -hs Projects/
```

# How to upgrade device firmware from the command line
```bash
fwupdmgr update
```