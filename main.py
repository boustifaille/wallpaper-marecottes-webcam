import json
import os
import urllib.request
import requests
import wallpaper
import datetime

# TODO: only update image if hash changes

BASE_URL = "https://valleedutrient.roundshot.com/telemarecottes/structure.json"


class WallpaperHelperHijack(wallpaper.WallpaperHelper):
    def get_desktop_environment(self):
        return "xfce"


def get_image():

    headers = {
        "Host": "valleedutrient.roundshot.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Referer": "https://valleedutrient.roundshot.com/telemarecottes/",
        "Cookie": "rs-ga-stats=disabled",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
    }

    session = requests.Session()

    session.cookies.update({"rs-ga-stats": "disabled"})

    response = session.get(BASE_URL, headers=headers)

    if response.status_code != 200:
        print("Error, status code: ", response.status_code)
        return None

    data = json.loads(response.text)
    image_url = data["images"][0]["structure"]["full"]["url_full"]

    # get the last file used
    picture_fullpath = "/home/antho/Documents/code/marecottes/picture.jpg"
    image_fullpath = "/home/antho/Documents/code/marecottes/image.jpg"

    picture_last_mod = os.path.getmtime(picture_fullpath)
    image_last_mod = os.path.getmtime(image_fullpath)
    
    finalpath = picture_fullpath if image_last_mod > picture_last_mod else image_fullpath

    urllib.request.urlretrieve(image_url, finalpath)

    return finalpath


def set_wallpaper(image_path):
    path = os.path.abspath(image_path)

    wallpaperHelper = WallpaperHelperHijack()
    wallpaperHelper.set_wallpaper(path, True)


def main():

    image = get_image()
    result = 'no image found'

    if image is not None:
        set_wallpaper(image)
        result = 'sucessfull'

    print(f"{datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y, %H:%M:%S')}: {result}")


if __name__ == "__main__":
    main()
