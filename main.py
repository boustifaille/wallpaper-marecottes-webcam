import requests
import os
import wallpaper
import json
import urllib.request

BASE_URL = "https://valleedutrient.roundshot.com/telemarecottes/structure.json"


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


    session.cookies.update({
        "rs-ga-stats": "disabled"
    })

    response = session.get(
        BASE_URL,
        headers=headers
    )

    if response.status_code != 200:
        print('Error, status code: ', response.status_code)
        return None


    data = json.loads(response.text)
    image_url = data["images"][0]['structure']['full']['url_full']

    urllib.request.urlretrieve(image_url, '/home/antho/Documents/code/marecottes/image.jpg')

    return True


def set_wallpaper():
    # we need to reset it to another file name : https://gitlab.xfce.org/xfce/xfdesktop/-/issues/416
    path = os.path.abspath("/home/antho/Documents/code/marecottes/image.jpg")
    path_reset = os.path.abspath("/home/antho/Documents/code/marecottes/black.jpg")

    wallpaperHelper = wallpaper.WallpaperHelper()
    wallpaperHelper.set_wallpaper(path_reset, True)
    wallpaperHelper.set_wallpaper(path, True)



def main():

    result = get_image()
    if result is None: return

    set_wallpaper()
    print('Successful')



if __name__ == '__main__':
    main()
