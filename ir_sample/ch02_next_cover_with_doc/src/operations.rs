use std::collections::{BTreeMap, HashMap};
use crate::position::Position;


static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


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


#[allow(dead_code)]
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


pub fn first_doc(term: String, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    if posting_list.contains_key(&term) {
        if let Some(doc) = &posting_list[&term].first() {
            return doc.d;
        }
    }
    return NEG_INF;
}


pub fn last_doc(term: String, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    if posting_list.contains_key(&term) {
        if let Some(doc) = &posting_list[&term].last() {
            return doc.d;
        }
    }
    return INF;
}


pub fn next_doc(term: String, current: i32, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    if current == INF {
        return INF;
    }
    
    if current == NEG_INF {
        return first_doc(term, &posting_list);
    }

    let docs = &posting_list[&term];
    for doc in docs {
        if current < doc.d {
            return doc.d;
        }
    }
    return INF;
}


pub fn prev_doc(term: String, current: i32, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    if current == NEG_INF {
        return NEG_INF;
    }

    if current == INF {
        return last_doc(term, &posting_list);
    }

    let docs = &posting_list[&term];
    for doc in docs.iter().rev() {
        if current > doc.d {
            return doc.d;
        }
    }
    return NEG_INF;
}
