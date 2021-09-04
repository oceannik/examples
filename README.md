# Example configuration files and utilities for Oceannik

## Playbook for setting up the Master Node

To configure the Master Node semi-automatically using an Ansible Playbook, use the provided `setup-master-node.yml` playboook. 
This is na alternative to installing the required packages manually.


To define which host the playbook should be executed against, create a new *hosts file* (called an *inventory* in Ansible).

An example of a minimal hosts file is included below.
The user should replace the IP Address, the name of the user, and the path to the SSH key with the appropriate values.

```
[oceannik_master]
192.168.0.100

[oceannik_master:vars]
ansible_user=debian
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_python_interpreter=/usr/bin/python3
```

With this file in place, it is possible to execute the playbook using the following command:
```
ansible-playbook setup-master-node.yml -i hosts_file.ini
```

This playbook was tested using `ansible-core` version `2.11.4`. To install `ansible-core` using pip (requires both pip and Python 3 to be installed), issue the command below.

```
pip3 install ansible-core==2.11.4
```

## The example project

The example project is located under the [example-project/](example-project/) directory. 
This directory contains an `oceannik.yml` service configuration file that can be used to test scheduling deployments.

## The example app

The example app is part of the *example project*. It is included in the project service configuration, and the app itself is deployed during the process. 

The application is a simple Python HTTP Server that prints debug information and shows information about the current active environment, which is determined by environment variables injected by Oceannik during the run of a Deployment Strategy.
