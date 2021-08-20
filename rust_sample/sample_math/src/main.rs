fn main() {
    let a: f32 = 5.0/4.0;
    let b = a.log(2.0);
    let c = (2.0 as f32).log(2.0) + 1.0;
    println!("idf={}, tf={}, tfidf={}", b, c, b*c);
    println!("e={}", std::f32::consts::E);
    println!("Hello, world!");
}
