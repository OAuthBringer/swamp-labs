# swamp-labs

1. Home Automation brain - In Progress
1. Robotic Control Systems - To Do

## Docs

1. [Architecture](docs/ARCHITECTURE.md)
1. [Project](docs/PROJECT.md)

## Usage

### Requirements
OSX is only currently supported install path.

Make sure Docker OSX is installed

- brew install minikube
- brew install kubectl


### Create 

```
make
```

### Check status

```
make status
```


### Delete

```
make delete
```

### Expose home assistant service to local IP

Run this in a dedicated terminal.

```
make home-assistant-available
```
