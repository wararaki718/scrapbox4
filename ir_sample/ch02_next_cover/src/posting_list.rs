use std::collections::HashMap;


pub fn get_posting_list(docs: &Vec<String>) -> HashMap<String, Vec<i32>> {
    let mut posting_list: HashMap<String, Vec<i32>> = HashMap::new();
    let mut offset: i32 = 1;
    for doc in docs {
        let terms = doc.split(" ");
        for t in terms {
            let term = String::from(t);
            if !posting_list.contains_key(&term) {
                posting_list.insert((&term).to_string(), Vec::new());
            }
            if let Some(v) = posting_list.get_mut(&term) {
                v.push(offset);
            }
            offset += 1;
        }
    }
    return posting_list;
}
