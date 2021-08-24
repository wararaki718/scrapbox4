use std::collections::HashMap;


#[derive(Debug)]
pub struct Position {
    d: i32,
    f_td: i32,
    p: Vec<i32>
}

impl Position {
    pub fn new(d: i32, f_td: i32, p: Vec<i32>) -> Self {
        Self {
            d, f_td, p
        }
    }
}

pub fn get_posting_list_positional_index(docs: &Vec<String>) -> HashMap<String, Vec<Position>> {
    let mut posting_list: HashMap<String, Vec<Position>> = HashMap::new();
    for (i, doc) in docs.iter().enumerate() {
        let mut positions: HashMap<String, Vec<i32>> = HashMap::new();
        let terms = doc.split(" ");
        for (j, term) in terms.enumerate() {
            if !positions.contains_key(&term.to_string()) {
                positions.insert(term.to_string(), Vec::new());
            }
            if let Some(v) = positions.get_mut(&term.to_string()) {
                v.push((j+1) as i32);
            }
        }
        for (term, indices) in &positions {
            if !posting_list.contains_key(&term.to_string()) {
                posting_list.insert(term.to_string(), Vec::new());
            }
            if let Some(v) = posting_list.get_mut(&term.to_string()) {
                v.push(Position::new((i+1) as i32, indices.len() as i32, indices.to_vec()));
            }
        }
    }

    return posting_list;
}