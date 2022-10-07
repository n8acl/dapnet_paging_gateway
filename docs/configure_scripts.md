# Configure the Scripts

Once you have your all the credentials you need, have cloned the repo and installed everything, you can now start configuring the scripts. 

## Configure DAPNET.json

First, open the ```dapnet.json``` file in the editor of your choice.

In this file you will see the following:

```json
{
    "my_creds": 
         {
             "username": "DAPNET USERNAME HERE",
             "password": "DAPNET PASSWORD HERE",
             "tx_group": "all"
         }
 }
```

Put your DAPNET Username and Passwords into the correct fields and save the file and close it.

## Configure dapnet_callsign_data_load.py

Next, open the ```dapnet_callsign_data_load.py``` file in the editor of your choice. Scroll down till you find a section like so:

```python
#############################
##### Define Variables

# define mysql connection variables
mysql_host = 'MYSQL HOST IP ADDRESS'
mysql_user = 'MYSQL USERNAME'
mysql_password = 'MYSQL PASSWORD'
```

Enter the MySQL IP Address, Username and password as asked in the appropriate places. Do NOT change anything below the line marked:

```python
#############################
##### DO NOT CHANGE BELOW
```

If you do, you will break your script. Remember the Disclaimer on the front page of the Wiki.

## Configure dapnet_paging_gateway_*.py

Next, open one of the paging gateway scripts files in the editor of your choice. 

* If you want to set this up for just yourself, use ```dapnet_paging_gateway_su.py```
* If you want to set this up for multiple people, use ```dapnet_paging_gateway_mu.py```

Scroll down till you find a section like so:

```python
#############################
##### Define Variables

# define mysql connection variables
mysql_host = 'MYSQL HOST IP ADDRESS'
mysql_user = 'MYSQL USERNAME'
mysql_password = 'MYSQL PASSWORD'
```

Just like with the callsign data loader, enter the MySQL IP Address, Username and password as asked in the appropriate places. Do NOT change anything below the line marked:

```python
#############################
##### DO NOT CHANGE BELOW
```

If you do, you will break your script. Remember the Disclaimer on the front page of the Wiki.

## Set Callsign Data load for automatic loading

Remember how I said that there is some data that is pulled from vairous sources to achieve this magic. This is the part that does it.

Once you have the scripts configured and the database built, we will need to load the data from the web.

This is something that should happen on a regulr basis to make sure everything is up to date. Let's go ahead and load the data now.

Run the following wherever you have the ```dapnet_callsign_data_load.py``` file sitting. This could be on your FreePBX box or this could be on another computer. 

```bash
python3 dapnet_callsign_data_load.py
```

This will take a bit to run and it should give feedback as to the progress. It should not take too terribly long, but it can take 10 - 15 minutes to parse all the data.

Because this can take a while to run, I would suggest setting up a cron job to run this over night. The cron job I use is:

```bash
0 2 * * * python3 scripts/dapnet_callsign_data_load.py
```

This will fire my script every day at 2:00 am and do the data load then.

Next we need to configure FreePBX/Asterisk.