import requests
import os
import wallpaper

BASE_URL = "https://valleedutrient.roundshot.com/download/[num]/?path=telemarecottes"


def get_last_number():

    number = 0

    with open('number.txt', 'r') as f:
        number = f.read()
    

    number = int(number)

    return number

def write_number(num):
    with open("number.txt", 'w') as f:
        f.write(str(num))


def get_image(number):


    url = BASE_URL.replace('[num]', str(number))

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Priority": "u=4",
        "Referer": "https://valleedutrient.roundshot.com/telemarecottes/"
    }

    session = requests.Session()


    session.cookies.update({
        "rs-cookie": "accepted",
        "rs-ga-stats": "disabled"
    })

    response = session.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        print('Error, status code: ', response.status_code)
        return None

    with open("image.jpg", "wb") as f:
        f.write(response.content)

    write_number(number)

    return True


def set_wallpaper():
    # we need to reset it to another file name : https://gitlab.xfce.org/xfce/xfdesktop/-/issues/416
    path = os.path.abspath("./image.jpg")
    path_reset = os.path.abspath("./black.jpg")

    wallpaperHelper = wallpaper.WallpaperHelper()
    wallpaperHelper.set_wallpaper(path_reset, True)
    wallpaperHelper.set_wallpaper(path, True)



def main():

    result = None

    while result is None:
        num = get_last_number()
        result = get_image(num)
        write_number(num+1)


    set_wallpaper()



if __name__ == '__main__':
    main()
