# Installation/Setup

Remember that all the commands shared here are for Linux. So if you want you can run this on a Linux Server or even a Raspberry Pi. In fact I have mine running on a Raspberry Pi 3B+.

If you want to run this on a Windows or Mac machine, you will need to be able to install Python3, be familiar installing from a requirements.txt and be familiar with how to schedule a recurring task in those OS's.

## What you will need

You will need a few things to be able to configure the scripts.

* Your DAPNET Username and Password
* The Username, Password and IP Address of your MySQL Instance

## Obtaining DAPNET Keys

The first step in this process is to get your DAPNET Credentials. If you are already a DAPNET user, you should already have your Username and Password from them. 

If you are not currently a DAPNET user, head over to [hampager.de](https://hampager.de) and go through the signup process. The website is in German, so you will need to be able to either read German or translate the webpage. The approval process could take a couple of days and does take a few steps, so you may want to start on that now... I will wait... Are you back? Ok.

## Getting the Script

The next step is cloning the repo to get all the files and then installing the needed libraries for the scripts to work properly.

This is probably the easiest step to accomplish.

Log into your FreePBX box and run the following commands:

```bash
sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade

sudo apt-get install python3 python3-pip git

git clone https://github.com/n8acl/dapnet_paging_gateway.git

cd dapnet_paging_gateway

pip3 install -r requirements.txt
```

If you are going to run the callsign loader script on another computer, you will need to move that script and the ```requirements.txt``` file to that machine and install the requirements there as well.

Now let's setup the MySQL Database first.