use std::collections::HashMap;


pub fn build_index(texts: Vec<String>, dictionary: HashMap<String, usize>) {
    let mut position: usize = 1;
    let mut records: Vec<(usize, usize)> = Vec::new();

    for text in texts {
        for term in text.split(" ") {
            if let Some(term_id) = dictionary.get(term) {
                records.push((*term_id, position));
            }
            position += 1;
        }
    }
    records.sort_by_key(|key| key.0);

    // 本来ならここでディスクに書き込む
    println!("(termID, position)");
    for record in records {
        println!("{:?}", record);
    }
}