mod func;

use func::create_sample;

fn main() {
    let name = String::from("test");
    let sample = create_sample(name);
    println!("name: {}", sample.name);
    println!("DONE");
}
