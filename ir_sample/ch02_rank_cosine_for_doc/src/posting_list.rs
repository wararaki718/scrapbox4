use std::collections::HashMap;
use ch02_rank_cosine_for_doc::position::Position;


pub fn get_posting_list_positional_index(docs: &Vec<String>) -> HashMap<String, Vec<Position>> {
    let mut posting_list: HashMap<String, Vec<Position>> = HashMap::new();
    for (i, doc) in docs.iter().enumerate() {
        let mut positions: HashMap<String, Vec<i32>> = HashMap::new();
        let terms = doc.split(" ");
        for (j, t) in terms.enumerate() {
            let term = &String::from(t);
            if !positions.contains_key(term) {
                positions.insert((&term).to_string(), Vec::new());
            }
            if let Some(v) = positions.get_mut(term) {
                v.push((j+1) as i32);
            }
        }
        for (t, indices) in &positions {
            let term = &String::from(t);
            if !posting_list.contains_key(term) {
                posting_list.insert((&term).to_string(), Vec::new());
            }
            if let Some(v) = posting_list.get_mut(term) {
                v.push(Position::new((i+1) as i32, indices.len() as i32, indices.to_vec()));
            }
        }
    }

    return posting_list;
}