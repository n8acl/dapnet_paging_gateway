# Configure Database

For this to run and work, there is a database component to this that loads some data on a regular basis. So the first thing we need to do is setup the database on your database server.

Note that for this step, you should already have a supported Database System installed and configured. The installation and configuration is out side the scope of this documentation and can be found online.

You also should be a little familiar with Databases and SQL in general to do this part. If not, find a friend who is capable and ask them to help with it (note I didn't say do it for you).

## Create the Database

To create the database, SSH into where you cloned the repo and make sure you are in the scripts directory.

```bash
cd dapnet_paging_gateway

cd scripts
```

Then run the ```install.py``` script. This will create the database, the tables and any local directories needed for data downloading and processing.

```bash
python3 install.py
```

## Preload some of the data - Multi-User Only

If you are going to use the script in Multi-User mode, you will need to preload some data to the database. These are extensions that people could be calling from, so that the script can pair their extension with the correct Callsign. An example of this would be, say you have multiple Hams at home that could potentially use this system, you will need to add their extension and callsign to the database manually so that the gateway knows what callsign to associate with that extension.

To do this, run the following (modified of course to fix your situation) in your Database Server:

```sql
insert into dapnet.dbo.ext_data (extension,callsign)
values('101','W1ABC'),
('102','WA2ABD')
```

Make sure to add as many extensions as needed for your PBX.


## Test the Scripts

Now you have everything installed and configured, let's try running the script.

Using your DMR ID run the following (making sure you are in the scripts folder):

Replace the following the command first:
* ```myDMR```: your DMR ID. If you have multiple ones, just choose one, it does not matter.
* ```test_ext```: If you are in Single user Mode, set this to 12345. If you are in Multi-User Mode, set this to an extension you added earlier.

```bash
python3 dapnet_paging_gateway.py myDMR 8675309 test_ext
```

You should get a page on your pager, or check Pi-Star, or check the DAPNET website and you should see a message to you formatted Simliar to ```N8ACL: Call me at 8675309``` but it should be your callsign.

If you get the message, you have everything configured correctly thus far.

Now it's time to [configure FreePBX/Asterisk](https://n8acl.github.io/dapnet_paging_gateway/configure_freepbx/).