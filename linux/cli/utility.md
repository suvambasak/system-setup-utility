# CLI cheatsheet

## GOTO
- [PDF](#pdf)
- [Image](#image)
- [Network printer](#nw-printer)
- [FFmpeg](#ffmpeg)
- [Timeshif](#timeshif)
- [Disk](#disk)
- [Firmware](#firmware)


----

# PDF
Merge multiple PDF file into one file

```bash
pdfunite 1.pdf 2.pdf 3.pdf final.pdf
```

# Image
Resize image file

```bash
convert -resize 30% file.jpg new_file.jpg
```

# NW printer

```bash
lp -d KD-304_original -o sides=two-sided-long-edge ~/path/to/paper.pdf
```

```bash
lp -d clp.cse.iitk.ac.in -o sides=two-sided-long-edge ~/path/to/paper.pdf
```

----
# FFmpeg
Create a video from frames (png)

```bash
ffmpeg -framerate 3 -pattern_type glob -i '/media/suvam/Storage/LEO-NET/toffset_0/*.png' -c:v libx264 -pix_fmt yuv420p output.mp4
```


----
# Timeshif

Open TimeShift in remote desktop (xrdp)
```bash
sudo /bin/bash -c "export XAUTHORITY=\"${HOME}/.Xauthority\" && timeshift-gtk"
```

----
# Disk

Available space device wise
```bash
df -h
```

Directory size
```bash
du -hs Projects/
```


# Firmware
Information about available updates (metadata)
```bash
sudo fwupdmgr refresh
```

Check for firmware updates
```bash
sudo fwupdmgr get-updates
```

Install Available Updates
```bash
sudo fwupdmgr update
```
