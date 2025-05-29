# Configure FreePBX/Asterisk

Now that we have the scripts configured and the database built, the last step before we are done is to configure FreePBX and Asterisk.

Note that you should already have a FreePBX/Asterisk instance installed and configured. That is outside the scope of this document/project. There are plenty of guides online to help you do that.

You will need to connect to your FreePBX box to edit files and move files around during this next process. You should be comfortable with editing files in an editor like Visual Studio Code and with working on the Linux command line.

## Disclaimer

Know that you modify your FreePBX installation at your own risk. Make sure you make backups and everything before you start. 

This install is not for the faint of heart. This script is a bit of an involved install and if you are not comfortable with working in MySQL or making changes to your FreePBX/Asterisk System, you can break things badly.

You have been thusly warned.

## Move scripts and files

First we need to move some of the files around out of the repo folder to put them into the right places so that what needs to access them can.

SSH into your FreePBX box.

Run the following in order to move the scripts, sounds and json file:

```bash
mkdir /var/lib/asterisk/scripts/dapnet

mkdir /var/lib/asterisk/sounds/custom/dapnet_gateway

cd dapnet_paging_gateway

cp -R /scripts/* /var/lib/asterisk/scripts/dapnet/*

cp /sounds/dapnet_gateway/* /var/lib/asterisk/sounds/custom/dapnet_gateway/*
```

Verify your work. Make sure all the scripts are in the Asterisk dapnet Scripts folder and that there is a directory called src with 4 scripts in it in the dapnet folder and the sounds are in the sounds folder and the 

## Modify the extensions_custom.conf

Next, we need to modify the ```extensions_custom.conf``` file. Open that in your editor.

Next copy the following stanza into that file:

```bash
;# // BEGIN DAPNET
exten => 327638,1,Answer
exten => 327638,n,Wait(1)
exten => 327638,n,Set(TIMEOUT(digit)=8)
exten => 327638,n,Set(TIMEOUT(response)=10)
exten => 327638,n,Set(VOLUME(TX)=10)
exten => 327638,n,Playback(/var/lib/asterisk/sounds/custom/dapnet_gateway/dpg_welcome)
exten => 327638,n,Wait(1)
exten => 327638,n,Playback(/var/lib/asterisk/sounds/custom/dapnet_gateway/dpg_enter_dmrid)
exten => 327638,n,Set(VOLUME(TX)=0)
exten => 327638,n,Read(RIC,beep,8)
exten => 327638,n,Set(VOLUME(TX)=10)
exten => 327638,n,Playback(/var/lib/asterisk/sounds/custom/dapnet_gateway/dpg_enter_callback)
exten => 327638,n,Set(VOLUME(TX)=0)
exten => 327638,n,Read(CALLBACK,beep,12)
exten => 327638,n,System(python3 /var/lib/asterisk/scripts/dapnet/dapnet_paging_gateway.py ${RIC} ${CALLBACK} ${CALLERID(number)})
exten => 327638,n,Set(VOLUME(TX)=10)
exten => 327638,n,Playback(/var/lib/asterisk/sounds/custom/dapnet_gateway/dpg_thank_you)
exten => 327638,n,Wait(1)
exten => 327638,n,Hangup
;# // END DAPNET
```

Save that and exit.

Then restart Asterisk.

## Configure FreePBX

Now we need to tell FreePBX about this new extension. It will not pick it up automatically.

* Log into your FreepBX GUI in a web browser.
* Click on ```Custom Extensions```
* Click ```Add Extension```
* In the ```Custom Extension``` field, enter ```327638``` (spells DAPNET on the phone keypad)
* In the ```Description``` field, enter ```DAPNET``` so you know what this is later.
* Click ```Submit```
* Click ```Apply Changes```

That should do it. Now we should be able to [send a page to a user](https://n8acl.github.io/dapnet_paging_gateway/using_the_gateway/).