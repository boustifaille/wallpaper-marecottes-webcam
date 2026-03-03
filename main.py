import requests
import os
import wallpaper
import json
import urllib.request

BASE_URL = "https://valleedutrient.roundshot.com/telemarecottes/structure.json"


class WallpaperHelperHijack(wallpaper.WallpaperHelper):
    def get_desktop_environment(self):
        return 'xfce'
    

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


    # get the last file used
    picture_fullpath = f"/home/antho/Documents/code/marecottes/picture.jpg"
    image_fullpath = f"/home/antho/Documents/code/marecottes/image.jpg"

    picture_last_mod = os.path.getmtime(picture_fullpath)
    image_last_mod = os.path.getmtime(image_fullpath)

    if image_last_mod > picture_last_mod: fullpath = picture_fullpath
    else: fullpath = image_fullpath

    print(fullpath)

    urllib.request.urlretrieve(image_url, fullpath)

    return fullpath


def set_wallpaper(image_path):
    path = os.path.abspath(image_path)

    wallpaperHelper = WallpaperHelperHijack()
    wallpaperHelper.set_wallpaper(path, True)



def main():

    result = get_image()
    if result is None: return

    set_wallpaper(result)
    print('Successful')



if __name__ == '__main__':
    main()
