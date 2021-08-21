fn main() {
    let a: Vec<i32> = vec![1, 2, 3, 4];
    let b: Vec<i32> = vec![1, 2, 3, 4];

    for i in a.iter().map(|x| 2*x) {
        println!("{}", i);
    }

    for (i, j) in a.iter().zip(b.iter()) {
        println!("{} {}", i, j);
    }

    for i in a.iter().zip(b.iter()).map(|(x, y)| x*y) {
        println!("{}", i);
    }

    let c: i32 = a.iter().zip(b.iter()).map(|(x, y)| x*y).sum();
    println!("{}", c);
    println!("DONE");
}
