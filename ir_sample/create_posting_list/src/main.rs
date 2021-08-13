use std::collections::HashMap;
use std::fs::File;
use std::io::Read;


fn main() {
    let filename = "text.txt";
    let mut file = match File::open(filename) {
        Err(why) => panic!("Could not open {}: {}", filename, why),
        Ok(file) => file
    };

    let mut contents = String::new();
    match file.read_to_string(&mut contents) {
        Err(why) => panic!("Could not read {}: {}", filename, why),
        Ok(_) => ()
    };

    // create posting list
    let mut posting_list: HashMap<String, Vec<i32>> = HashMap::new();
    let mut index: i32 = 1;
    for line in contents.split("\n") {
        for word in line.split(" ") {
            if !posting_list.contains_key(&word.to_string()) {
                posting_list.insert(word.to_string(), Vec::new());
            }
            if let Some(v) = posting_list.get_mut(&word.to_string()) {
                v.push(index);
            }
            index += 1;
        }
    }
    println!("{:?}", posting_list["first"]);

    println!("DONE");
}
