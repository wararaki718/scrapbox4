use std::collections::HashMap;

use crate::posting::Posting;


pub fn get_posting_list(docs: &Vec<String>) -> HashMap<String, Vec<Posting>> {
    let mut posting_list: HashMap<String, Vec<Posting>> = HashMap::new();
    for (i, doc) in docs.iter().enumerate() {
        let terms = doc.split(" ");
        for (j, t) in terms.enumerate() {
            let term = &String::from(t);
            if !posting_list.contains_key(term) {
                posting_list.insert((&term).to_string(), Vec::new());
            }
            if let Some(v) = posting_list.get_mut(term) {
                v.push(
                    Posting::new((i+1) as i32, (j+1) as i32)
                );
            }
        }
    }

    return posting_list;
}
