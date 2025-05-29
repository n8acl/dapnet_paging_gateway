# DAPNET Paging Gateway

**NOTE**: I have unarchived this to fix somethings in the scripts. While I still am not running a PBX, I can fix the Python scripts and need to include the SQL script. Updates soon.

---

An old style paging gateway for DAPNET for use with FreePBX/Asterisk

Remember the days of calling a pager number, entering your callback number or leaving a voicemail and that message being sent to the end user? Well those days are kind of back... at least for Hams. This is what the kids are calling "Retro-tech" today.

The Decentralized Amateur Paging Network (DAPNET) is a paging network that was setup by some hams in Germany and has slowly been moving around the world in popularity. While it has a large user base outside the US, it is gaining some traction in the US as well. It utilizes the old POCSAG protocol to send Alpha-Numeric messages to old Alpha-Numeric text pagers.

It can breathe new life into those old Alpha-Numberic Pagers that we used to all carry around. It can use your Pi-Star hotspot to send a page or a high profile repeater. More information about DAPNET can be found at [https://hampager.de](https://hampager.de). The site is in German, so you will need to translate it to your language, or be able to read German.

The DAPNET Paging Gateway provides the ability to simulate the old paging gateway callback system from your FreePBX PBX system to DAPNET.

This Wiki is designed as a user guide for the end users of the software.

This software is for use by Amateur Radio Operators Only.

For information about installing and configuring, please see [https://n8acl.github.io/dapnet_paging_gateway/](https://n8acl.github.io/dapnet_paging_gateway/) which is the Wiki for the project.

## What this project does not do

This project does not:

* Send to pagers on the PSTN
* Allow for voicemails to pagers
* Allow for Text messages to Alpha pagers.

## What this project does do

This project does:

* Allow a user to enter a callback number and then a page will be sent. That's it.

### Contact Me

If you have questions, please feel free to reach out to me. You can reach me in one of the following ways:

* Discord: Ravendos
* Mastodon: @n8acl@mastodon.radio
* E-mail: n8acl@qsl.net

If you reach out to me and have an error, please include what error you are getting and what you were doing. I may also ask you to send me certain files to look at. Otherwise just reach out to me :).

