# Wallpaper Marécottes

Sets the Linux desktop wallpaper to the latest live image of the Les Marécottes webcam:
<https://valleedutrient.roundshot.com/telemarecottes/>

## How it works

`main.py` asks the Roundshot private API (`structure.json`) for the URL of the current
webcam image, downloads it, and hands it to `wallpaper.py`, which sets it as the desktop
background (XFCE).

The image alternates between `image.jpg` and `picture.jpg` on each run. This forces the
window manager to actually reload the wallpaper instead of ignoring an unchanged file.

## Usage

```bash
pip install requests   # PyGObject (gi) is also required for XFCE
python3 main.py
```

## Automate with cron

`launch.sh` exports the D-Bus session address (needed when running from cron) and runs the
script:

```cron
*/10 * * * * /home/antho/Documents/code/marecottes/launch.sh >> /home/antho/Documents/code/marecottes/cron.log 2>&1
```

## What changed

The project was rewritten in **Python** and now queries the Roundshot **private API**
(`structure.json`, with the `rs-ga-stats=disabled` cookie) to always fetch the latest image.
