# Create service

```bash
sudo mv ~/autologin.service /etc/systemd/system/autologin.service
```

```bash
sudo systemctl daemon-reload
```

```bash
sudo systemctl enable autologin.service
```

```bash
sudo systemctl start autologin.service
```

```bash
sudo systemctl status autologin.service
```
