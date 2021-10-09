use std::collections::{HashMap, HashSet};


pub fn build_index(texts: Vec<String>, dictionary: HashMap<String, Vec<String>>) {
    let mut position: usize = 0;
    let mut posting_list: HashMap<String, Vec<usize>> = HashMap::new();
    let mut entries: HashSet<String> = HashSet::new();

    for text in texts {
        for term in text.split(" ") {
            if !posting_list.contains_key(term) {
                posting_list.insert((&term).to_string(), Vec::new());
            }

            if dictionary.contains_key(term) {
                entries.insert((&term).to_string());
            }

            if let Some(v) = posting_list.get_mut(term) {
                v.push(position);
            }
            position += 1;
        }
    }

    let mut terms: Vec<String> = entries.into_iter().collect();
    terms.sort();

    // 本来ならここでディスクに書き込む
    for term in terms {
        println!("{}: {:?}", term, posting_list[&term]);
    }
}