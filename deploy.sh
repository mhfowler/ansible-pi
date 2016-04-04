#!/usr/bin/env bash
ansible-playbook ansible-pi/playbook.yml -i ansible-pi/hosts --ask-pass --sudo -c paramiko
