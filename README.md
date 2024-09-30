# RODGER

This repository provides a setup for building and running a Docker container for RODGER. Follow the instructions below to set up your environment, build the Docker image, and run the container.

## Prerequisites

Ensure you have the following installed:
- Docker
- NVIDIA GPU and drivers (if using `--gpus=all` for GPU support)
- NVIDIA Container Toolkit (if using GPU support with Docker)

## Setup Instructions

### Step 1: Edit the Environment File
Before building the Docker image, you need to adjust the environment file by specifying the correct path to your RODGER directory.

1. Open the environment file in your text editor.
2. Modify the `SCRIPT_PATH` variable to point to your RODGER directory. For example:

    ```bash
    # Path to the directory containing the Dockerfile
    SCRIPT_PATH="/path/to/RODGER"
    ```

### Step 2: Source the Environment to `.bashrc`
To make the custom functions in the environment file available in your terminal sessions, you need to source it in your `.bashrc`.

1. Add the following line to your `.bashrc` file, replacing `PATH_TO_ENVIRONMENT_FILE` with the path to your environment script:

    ```bash
    echo "source $/path/to/environment/file" >> ~/.bashrc
    ```

2. Open a new terminal or run the following command to apply the changes immediately:

    ```bash
    source ~/.bashrc
    ```

### Step 3: Build the Docker Image
Once your environment is set up, you can build the Docker image with the following command:

```bash
make_rodger rodger_container ./path/to/RODGER/RODGER_src
```


### Step 4: Start the container
You can start the container with the following command (note that the container will start, but you will need to open a terminal):

```bash
start_container rodger_container
```
### Step 5: Open the terminal
You can open the terminal executing the started container with the following command:

```bash
open_terminal rodger_container
```

### Delete the container
You can delete the container with the following command:

```bash
delete_container rodger_container
```
