use std::collections::HashMap;

use crate::posting::Posting;
use crate::operations::{docid, first, last, next, prev};


static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;

#[allow(dead_code)]
pub fn first_doc(term: String, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    return docid(first(term, &posting_list));
}


#[allow(dead_code)]
pub fn last_doc(term: String, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    return docid(last(term, &posting_list));
}


pub fn next_doc(term: String, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if docid(current) == INF {
        return INF;
    }

    let mut position = current;
    while docid(position) == docid(current) {
        position = next((&term).to_string(), position, &posting_list);
    }

    return docid(position);
}


pub fn prev_doc(term: String, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if docid(current) == NEG_INF {
        return NEG_INF;
    }

    let mut position = current;
    while docid(position) == docid(current) {
        position = prev((&term).to_string(), position, &posting_list);
    }

    return docid(position);
}
