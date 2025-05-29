# Configure the Scripts

Once you have your all the credentials you need, have cloned the repo and installed all the libraries, you now need to configuring the scripts. 

## Configure config.json

First, open the ```config.json``` file in the editor of your choice.

In this file you will see the following:

```json
{
    "dapnet": {
        "username": "DAPNET USER NAME",
        "password": "DAPNET PASSWORD",
        "tx_group": "all"
    },
    "database": {
        "rdbms_type": "DB SERVER TYPE",
        "credentials": {
            "username": "DB SERVER USERNAME",
            "password": "DB SERVER PASSWORD",
            "host": "FQDN or IP ADDRESS OF DB INSTANCE",
            "db": "DAPNET"
        }
    },
    "gateway_mode": 1
}
```

***Settings Definitions***:
* ```dapnet``` - This section is your DAPNET Credentials
    * ```username```: This is your DAPNET Username, usually your callsign.
    * ```password```: This is your DAPNET Password.
    * ```tx_group```: This is the DAPNET tx_group to send the messages to. This is usually a regional setting. You will need to look this up on DAPNET to find out where the best place to send the messages is. Try to avoid the ```all``` group to keep from hitting every transmitter connected to DAPNET.
* ```database``` - This section is your Database Server credentials.
    * ```rdbms_type```: This is the type of Database Server you are using. 
        * Supported Types
            * ```mssql``` - MS SQL Server
            * ```mysql``` - MySQL/MariaDB
            * ```postgresql``` - PostgreSQL
            * ```sqlite``` - SQLite (built in Python DB)
    * ```credentials```: These are the credentials for your DB Instance
        * ```username```: Database Username
        * ```password```: Database Password
        * ```host```: FQDN or IP address of your Database Instance
        * ```db```: Always needs to be DAPNET - ***DO NOT CHANGE THIS***. If you change this, it will break things.
* ```gateway_mode```: This is the mode that the gateway should work in. This defines whether it is in Single-User (personal) or Multi-User (many users like a Cloud PBX) mode.
    * ```1```: Single-User Mode
    * ```2```: Multi-User Mode

Make your settings changes and then save the file.

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

Next we need to [configure the Database](https://n8acl.github.io/dapnet_paging_gateway/configure_database/).