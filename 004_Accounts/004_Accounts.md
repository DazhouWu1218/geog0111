# 004 Setup, Accounts and logins

## Introduction

### NASA Earthdata login and password


Before you can use the material in these notebooks, you will need to register as a user at the [`NASA EarthData`](https://urs.earthdata.nasa.gov/users/new).

Once you have done that, make sure you know your `username` and `password` ready for below.

Some web resources require you to use a login and password. In any publicly available files (like these notebooks) we do not want to expose sensitive information such information.

To that in these notes we can make use of stored passwords and usernames using the local [cylog](geog0111/cylog.py) package. 

Information is encrypted in a user read-only file in your home directory (mode `400`) and accessed through the `Cylog`  `login` function.

You need to store your username and password in a database file (that only you can access) to be able to make convenient use oof the notes in later classes.

You can do this by running through the following cell, and responding as appropriate.


```python
from geog0111.cylog import Cylog

sites = ['https://n5eil01u.ecs.nsidc.org',\
         'https://urs.earthdata.nasa.gov',\
        'https://e4ftl01.cr.usgs.gov']

l = Cylog(sites)
test = l.login()
```

If you are interested, you can see the help page for `Cylog`. It shows, for instance, how to over-ride the current entry (e.g. if you have changed your password), by using `force=True`).


```python
from geog0111.cylog import Cylog
help(Cylog.login)
```

    Help on function login in module geog0111.cylog:
    
    login(self, site=False, force=False)
        Reads encrypted information from ~/{dest_path}/.cylog.npz
        
        Keyword arguments
        ----------
        site = False (so self.site is default)
               string of anchor URL for site to associate with username and
               password
        force = False
               force password re-entry for site
        
        Returns
        --------
        A tuple containing plain text (username,password) for (site or self.site)
    


You should be aware that the NASA servers this connects you to go down for maintenance on Wednesdays. You can ping the servers with the follwoing code:

### Test

You can run a test on your login to NASA Earthdata using the information you have stored this using `cylog` according to [004_Accounts](004_Accounts.md) for the site `https://e4ftl01.cr.usgs.gov`. We can test this with the following code if you set do_test to True:


```python
from geog0111.modis import test_login
assert test_login(do_test)
```

If this fails, you may have entered your account information incorrectly for `https://e4ftl01.cr.usgs.gov` (or it could just be Wednesday, in which case, don't run this again).

If you want to force the code to let you re-enter your credentials (e.g. you got it wrong before, or have changed them, or the test fails), then change the call to:

    cy = cylog(site,force=True)
    
and re-run.