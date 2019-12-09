# Tomyris
Named after an ancient Messagetean queen, Tomyris is an intelligent camera-based alarm system with a web interface. 

Tomyris is W.I.P, it's practically useless until it's developed further!

## Components

TO-DO

## Installation

Ensure Python 3.7 or newer is installed. Older versions may work, but are unsupported.
MySQL 15.0 or newer is recommended for the database.

### On Linux (systemd)
> This is the recommended method if you have systemd installed.

Run [`install.sh`](https://raw.githubusercontent.com/UltraFuture7000/Tomyris/master/install.sh) with root privileges if you wish to install Tomyris as a systemd service.
You do not need to clone the repository for this.

This should walk you through everything.

After installation, Tomyris' files will reside in ``/opt/tomyris`` and you can use the command ``tomyrisctl`` in any directory.

### Other operating systems/no systemd

On other operating systems, or if you're rebellious/can't use systemd, get ready; things are a little rougher.

You'll need to clone the repository first.

First, run ``pip install -r requirements.txt`` to install Tomyris' requirements.

Then, run ``python tomyriscore.py`` once to allow it to generate the configuration file.

Next, fill in `config.txt` with your database information (example below).

![Next, fill in `config.txt` with your database information.](imgs/example_config.png)


Tomyris should now be configured. You'll need to run ``python tomyriscore.py`` manually for as long as you want Tomyris to operate.
Every time you wish to run tomyrisctl, you must run ``tomyrisctl.py`` with Python and that'll open up tomyrisctl for you.

## Troubleshooting

> Help! tomyrisctl says "Unable to communicate with service" and/or I can't visit the webpage!

If you used the install script:
- Run `journalctl -u tomyris` to check for errors.

Otherwise:

- Check `tomyris.log` for errors.