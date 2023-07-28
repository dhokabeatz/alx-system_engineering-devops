# 0x05. Processes and Signals

![Linux](https://img.shields.io/badge/Linux-ubuntu-orange) ![Bash](https://img.shields.io/badge/Bash-v5.0-blue)

This is a sub-project of the ALX-Holberton School Low-level Programming curriculum, focusing on the concepts of processes and signals in Linux. In this project, we explore the basics of processes, how to create and manage them, and how to communicate with processes using signals.

## Project Overview

The project is divided into several tasks, each covering different aspects of processes and signals in Linux. Some of the key concepts explored in this project include:

- Creating new processes using the `fork()` system call.
- Managing processes with process IDs (PIDs).
- Handling signals, including sending and receiving signals between processes.
- Implementing signal handlers to respond to various signals.
- Using signals to communicate information or control the behavior of processes.

The tasks in this project are designed to provide a hands-on understanding of processes and signals in Linux and how they can be used for various purposes, such as inter-process communication and process synchronization.

## Project Structure

The repository is organized into multiple directories, each containing Bash scripts and C code files related to specific tasks. Here is an overview of the directory structure:

- `0x05-processes_and_signals/`: Root directory containing subdirectories for each task.
- `0x05-processes_and_signals/task_0/`: Directory containing the solution for Task 0.
- `0x05-processes_and_signals/task_1/`: Directory containing the solution for Task 1.
- `0x05-processes_and_signals/task_2/`: Directory containing the solution for Task 2.
- ...
- `0x05-processes_and_signals/task_n/`: Directory containing the solution for Task n.

Here are the key files and directories within each task directory:

- `0x05-processes_and_signals/task_n/README.md`: Markdown file containing a description of the task and its requirements.
- `0x05-processes_and_signals/task_n/script_name`: Bash script or C code file implementing the solution for the task.
- `0x05-processes_and_signals/task_n/script_name.c`: C code file, if applicable, for the solution.

## Getting Started

To get started with this project, you can follow these steps:

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/dhokabeatz/alx-system_engineering_devops.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x05-processes_and_signals
   ```

3. Explore the individual task directories to understand the specific requirements and objectives.

4. Review the Bash scripts and C code files within each task directory to see the implementations.

5. Optionally, compile any C code files using the appropriate compiler:

   ```bash
   gcc -Wall -Werror -Wextra -pedantic script_name.c -o executable_name
   ```

6. Test the Bash scripts and C programs to verify their functionality.

## Resources

- [Linux Processes (Linux Documentation)](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html#pid-max)
- [Interprocess Communication in Linux (IBM Developer)](https://developer.ibm.com/technologies/linux/tutorials/l-ipc/)
- [Linux Signals (Linux Documentation)](https://www.kernel.org/doc/html/latest/core-api/signal.html)
- [Linux `kill` Command (Linux Man Pages)](https://man7.org/linux/man-pages/man2/kill.2.html)

## Author

This project is implemented and maintained by [@dhokabeatz](https://github.com/dhokabeatz).