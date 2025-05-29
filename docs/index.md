Welcome to the DAPNET Paging Gateway for FreePBX!

Remember the days of calling a pager number, entering your callback number or leaving a voicemail and that message being sent to the end user? Well those days are kind of back... at least for Hams. This is what the kids are calling "Retro-tech" today.

The Decentralized Amateur Paging Network (DAPNET) is a paging network that was setup by some hams in Germany and has slowly been moving around the world in popularity. While it has a large user base outside the US, it is gaining some traction in the US as well. It utilizes the old POCSAG protocol to send Alpha-Numeric messages to old Alpha-Numeric text pagers.

It can breathe new life into those old Alpha-Numberic Pagers that we used to all carry around. It can use your Pi-Star hotspot to send a page or a high profile repeater. More information about DAPNET can be found at [https://hampager.de](https://hampager.de). The site is in German, so you will need to translate it to your language, or be able to read German.

The DAPNET Paging Gateway provides the ability to simulate the old paging gateway callback system from your FreePBX PBX system to DAPNET.

This Wiki is designed as a user guide for the end users of the software.

This software is for use by Amateur Radio Operators Only.

## Requirements

In order to use these scripts, you will need to have the following setup and configured:

* A Database server instance (seperate from the FreePBX database).
    * Supported Databases
        * MS SQL Server
        * MySQL/MariaDB
        * PostgreSQL
        * SQLite
* A FreePBX server instance

You should also:

* be comfortable with editing files in an editor like Visual Studio Code or some other editor
* be comfortable with the Linux command line


## Parts of the Software

The DAPNET Paging Gateway is made up of multiple parts, but only a few are needed to run:

* ```dapnet_callsign_data_load.py``` - This script loads the needed callsign data from DAPNET and RadioID.net. You can run this on your FreePBX instance if you would like, but it will would be better to run it on a seperate machine from the PBX.
* ```dapent_paging_gateway.py``` - This is the script that is called by FreePBX/Asterisk to send the message to DAPNET. This script supports use on both a Single user PBX (IE a personal at home PBX) and a Multi-User PBX (like one hosted in the cloud for multiple users to access like one of the Ham Radio VOIP Services.)

## Disclaimer

Know that you modify your FreePBX installation at your own risk. Make sure you make backups and everything before you start. 

This install is not for the faint of heart. This script is a bit of an involved install and if you are not comfortable with working in SQLc or making changes to your FreePBX/Asterisk System, you can break things badly.

You have been thusly warned.

## Thanks

I did want to say thanks to the people who, behind the scenes, helped me with research, testing, encouragement and even gave me the idea to do this. You know who you are.

### Contact Me

If you have questions, please feel free to reach out to me. You can reach me in one of the following ways:

* Discord: Ravendos#7364
* Mastodon: @n8acl@mastodon.radio
* E-mail: n8acl@qsl.net

If you reach out to me and have an error, please include what error you are getting and what you were doing. I may also ask you to send me certain files to look at. Otherwise just reach out to me :).
