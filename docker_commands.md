# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db

```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run --name server1 -v fastapi-db:/app/db -p 8000:8000 shopping-server1:v1
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run --name server2 -v fastapi-db:/app/db -p 8001:8000 shopping-server2:v1
```

### Run the container with bind-mount
```bash
docker run --name server2 -v fastapi-db:/app/db -v C:\Users\LENOVO\Desktop\week9_test\server2\data:/app/data -p 8001:8000 shopping-server2:v1
```