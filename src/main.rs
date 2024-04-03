use chrono::{DateTime, Local};

use wallpaper;

const BASE_URL: &str = "https://storage.roundshot.com/5b59b273448eb0.16775125";

fn main() {
    let today = Local::now();
    let url = &get_url_for_date(today);
    println!("Setting wallpaper to {url}");
    let result = wallpaper::set_from_url(url);

    match result {
        Err(err) => panic!("{}", err),
        Ok(_) => println!("Success")
    }
}
/*
fn download_image(url: String){

    let mut file = File::create("temp.jpg").expect("Failed to create file");

    let mut image = reqwest::blocking::get(&url)
        .expect("Failed to get image from url");

    if image.status() != 200 {
        panic!("Failed to get image from url {url}");
    }

    image.copy_to(&mut file)
        .expect("Failed to write to file");
}*/

fn get_url_for_date(date: DateTime<Local>) -> String {

    let minutes = date.format("%M").to_string().parse::<i32>().unwrap();
    let filename = date.format("%Y-%m-%d-%H").to_string() + &format!("-{}-00_half.jpg", minutes - minutes % 10);
    let foldername = date.format("%Y-%m-%d/%H").to_string() +&format!("-{}-00", minutes - minutes % 10);

    return format!("{}/{}/{}", BASE_URL, foldername, filename);
}