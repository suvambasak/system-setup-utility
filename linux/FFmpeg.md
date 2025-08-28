



## Create a video from frames (png)

```bash
ffmpeg -framerate 3 -pattern_type glob -i '/media/suvam/Storage/LEO-NET/toffset_0/*.png' -c:v libx264 -pix_fmt yuv420p output.mp4
```

## Increase volume

```bash
ffmpeg -i source.mp4 -af "volume=3.0" -c:v copy talk.mp4
```

## Remove noise

```bash
sudo apt install ffmpeg sox
```

Extract Audio from Video

```bash
ffmpeg -i name.mp4 -vn -ar 44100 -ac 2 audio.wav
```

Create a small sample of just the noise

```bash
ffmpeg -i audio.wav -ss 00:00:00.5 -t 1.5 noise-sample.wav
```

Generate the noise profile from this sample using SoX

```bash
sox noise-sample.wav -n noiseprof fan.noise.profile
```

Apply Noise Reduction

```bash
sox audio.wav cleaned-audio.wav noisered fan.noise.profile 0.25
```

Recombine Clean Audio with Original Video

```bash
ffmpeg -i name.mp4 -i cleaned-audio.wav -c:v copy -map 0:v:0 -map 1:a:0 final-video.mp4
```