use std::collections::{HashMap, HashSet};


pub fn get_posting_list_docid_index(docs: &Vec<String>) -> HashMap<String, Vec<i32>> {
    let mut posting_list: HashMap<String, Vec<i32>> = HashMap::new();
    for (i, doc) in docs.iter().enumerate() {
        let unique_terms: HashSet<&str> = doc.split(" ").into_iter().collect();
        for term in unique_terms {
            if !posting_list.contains_key(&term.to_string()) {
                posting_list.insert(term.to_string(), Vec::new());
            }
            if let Some(v) = posting_list.get_mut(&term.to_string()) {
                v.push((i+1) as i32);
            }
        }
    }

    return posting_list;
}

pub fn get_posting_list_frequency_index(docs: &Vec<String>) -> HashMap<String, i32> {
    let mut posting_list: HashMap<String, i32> = HashMap::new();
    for doc in docs {
        let unique_terms: HashSet<&str> = doc.split(" ").into_iter().collect();
        for term in unique_terms {
            if !posting_list.contains_key(&term.to_string()) {
                posting_list.insert(term.to_string(), 0 as i32);
            }
            if let Some(f) = posting_list.get_mut(&term.to_string()) {
                *f += 1 as i32
            }
        }
    }

    return posting_list;
}

pub fn get_posting_list_scheme_independent_index(docs: &Vec<String>) -> HashMap<String, Vec<i32>> {
    let mut posting_list: HashMap<String, Vec<i32>> = HashMap::new();
    let mut index: i32 = 1;
    for doc in docs {
        let terms = doc.split(" ");
        for term in terms {
            if !posting_list.contains_key(&term.to_string()) {
                posting_list.insert(term.to_string(), Vec::new());
            }
            if let Some(v) = posting_list.get_mut(&term.to_string()) {
                v.push(index);
            }
            index += 1;
        }
    }

    return posting_list;
}
