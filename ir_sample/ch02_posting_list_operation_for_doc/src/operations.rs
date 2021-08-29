use std::collections::{BTreeMap, HashMap};
use ch02_posting_list_operation_for_doc::position::Position;


pub fn docid(position: i32, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    let mut doc_offsets: BTreeMap<i32, i32> = BTreeMap::new();
    for value in posting_list.values() {
        for doc in value {
            if !doc_offsets.contains_key(&doc.d) {
                doc_offsets.insert(doc.d, 0);
            }
            if let Some(offset) = doc_offsets.get_mut(&doc.d) {
                *offset += doc.p.len() as i32;
            }
        }
    }

    let mut offset: i32 = 1;
    for key in doc_offsets.keys() {
        offset += doc_offsets[key];
        if position < offset {
            return *key;
        }
    }

    return -1 as i32;
}


pub fn offset(position: i32, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    let mut doc_offsets: BTreeMap<i32, i32> = BTreeMap::new();
    for value in posting_list.values() {
        for doc in value {
            if !doc_offsets.contains_key(&doc.d) {
                doc_offsets.insert(doc.d, 0);
            }
            if let Some(offset) = doc_offsets.get_mut(&doc.d) {
                *offset += doc.p.len() as i32;
            }
        }
    }
    
    let mut offset: i32 = 0;
    let mut offsets: Vec<i32> = vec![0, 0];
    for key in doc_offsets.keys() {
        offset += doc_offsets[key];
        offsets.push(offset);
    }

    for value in posting_list.values() {
        for doc in value {
            for p in &doc.p {
                if *p + offsets[doc.d as usize] == position {
                    return *p;
                }
            }
        }
    }

    return -1 as i32;
}
