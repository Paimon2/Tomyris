# Tomyris
Named after an ancient Messagetean queen, Tomyris is an intelligent camera-based alarm system with a web interface. 

## Installation

Ensure Python 3.7 or newer is installed. Older versions may work, but are unsupported.
MySQL 15.0 or newer is recommended for the database.

On Linux, run `./install.sh` with root privileges if you wish to install Tomyris as a systemd service.

On other operating systems, or if you're rebellious/can't use systemd, get ready; things are a little rougher.

You'll need to run ``python tomyris_core.py`` for as long as you want Tomyris to operate (hold up - see below!).

If you're not using the install script, run ``python tomyris_core.py`` once to allow it to generate the configuration file.
Then, fill in `config.txt` with your database information.