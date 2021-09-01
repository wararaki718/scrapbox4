mod user;
mod sample;

fn main() {
    let user = sample::create_user(1, String::from("hello"));
    println!("{:?}", user);
    println!("DONE");
}
