# Installation of Docker Desktop on Ubuntu

- Update the apt repository
```
sudo apt-get update
```

- Download - [Docker-desktop download link](https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64)

- Install command
```
sudo apt-get install ~/Downloads/docker-desktop-amd64.deb
```

- Launch Docker Desktop
To start Docker Desktop for Linux:

1. Open your Applications menu in Gnome/KDE Desktop and search for Docker Desktop.
2. Select Docker Desktop to start Docker. The Docker Subscription Service Agreement displays.
3. Select Accept to continue. Docker Desktop starts after you accept the terms.
Note that Docker Desktop won't run if you do not agree to the terms. You can choose to accept the terms at a later date by opening Docker Desktop.

Alternatively, open a terminal and run below to start the docker desktop:
```
systemctl --user start docker-desktop
```

- Check versions running on the machine
```
docker compose version
docker --version
docker version
```

- To stop Docker Desktop, select the Docker menu icon to open the Docker menu and select Quit Docker Desktop.
Alternatively, open a terminal and run:
```
systemctl --user stop docker-desktop
```

- To enable Docker Desktop to start on sign in, from the Docker menu, select Settings > General > Start Docker Desktop when you sign in to your computer.
Alternatively, open a terminal and run:
```
systemctl --user enable docker-desktop
```


[original source](https://docs.docker.com/desktop/install/ubuntu/)
