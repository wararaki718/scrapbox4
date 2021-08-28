use std::collections::{BTreeMap, HashMap};
use ch02_posting_list_doc::document::Document;


pub fn docid(position: i32, posting_list: &HashMap<String, Vec<Document>>) -> i32 {
    let mut doc_offsets: BTreeMap<i32, i32> = BTreeMap::new();
    for value in posting_list.values() {
        for doc in value {
            if !doc_offsets.contains_key(&doc.id) {
                doc_offsets.insert(doc.id, 0);
            }
            if let Some(offset) = doc_offsets.get_mut(&doc.id) {
                *offset += 1;
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


pub fn offset(position: i32, posting_list: &HashMap<String, Vec<Document>>) -> i32 {
    let mut doc_offsets: BTreeMap<i32, i32> = BTreeMap::new();
    for value in posting_list.values() {
        for doc in value {
            if !doc_offsets.contains_key(&doc.id) {
                doc_offsets.insert(doc.id, 0);
            }
            if let Some(offset) = doc_offsets.get_mut(&doc.id) {
                *offset += 1;
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
            let p: i32 = doc.offset + offsets[doc.id as usize];
            if p == position {
                return doc.offset;
            }
        }
    }

    return -1 as i32;
}