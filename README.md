# Practice Scripts for DevOps
This repository is a store for various scripts I've made to practice system configuration and task automation.


# Python Package Updater
Base Concept: Python script which determines which Linux distribution a host machine is running, and runs the update command against the corresponding package management. 
- Currently identifies Debian and Ubintu for apt and Fedora, Red Hat, and CentOS for yum.
- Additionally logs basic level information on the command to a log in "/var/log/pythonupdater" with the corresponding date and time
