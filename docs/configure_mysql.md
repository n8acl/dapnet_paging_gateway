# Configure MySQL

For this to run and work, there is a MySQL database component to this that loads some data on a regular basis. So the first thing we need to do is setup the database on your MySQL Server.

Note that for this step, you should already have MySQL installed on a computer and configured. That is outside the scope of this document/project, but there are plenty of guides online that will walk you through how to do it.

You also should be a little familiar with MySQL and SQL in general to do this part. If not, find a friend who is capable and ask them to help with it (note I didn't say do it for you).

## Create the Database

On your MySQL Database system, you will need to run the ```dapnet_database_install.sql``` script. You will also need to make sure that the MySQL user that you are going to use has full rights to the new database.

## Preload some of the data - Multi-User Only

If you are going to use the Multi-User script, you will need to preload some data to the database. These are extensions that people could be calling from, so that the script can pair their extension with the correct Callsign. An example of this would be, say you have multiple Hams at home that could potentially use this system, you will need to add their extension and callsign to the database manually so that the gateway knows what callsign to associate with that extension.

To do this, run the following (modified of course to fix your situation) in your MySQL Server:

```sql
insert into dapnet_freepbx.dbo.ext_data (extension,callsign)
values('101','W1ABC'),
('102','WA2ABD')
```

Make sure to add as many extensions as needed for your PBX.

Now you have everything installed and are ready to configure the scripts.