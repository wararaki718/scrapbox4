use std::collections::HashMap;


fn main() {
    let v = vec![1, 4, 6, 10];
    let v2 = vec![2, 9, 17, 22];
    let mut posting_list = HashMap::new();
    posting_list.insert("first", v);
    posting_list.insert("second", v2);

    let target = &posting_list["first"];
    for i in target {
        println!("{}", i);
    }
    println!("");

    for (key, value) in &posting_list {
        println!("{}", key);
        for i in value {
            println!("{}", i);
        }
    }

    println!("DONE");
}
