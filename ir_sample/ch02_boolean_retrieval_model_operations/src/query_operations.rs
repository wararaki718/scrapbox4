use std::collections::HashMap;
use std::cmp;

use crate::doc_operations::{next_doc, prev_doc};
use crate::posting::Posting;
use crate::query::Query;


pub fn doc_right(query: Query, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if query.is_edge() {
        return next_doc(query.term, current, &posting_list);
    }
    return match query.term.as_str() {
        "AND" => cmp::max(doc_right(query.get_right(), current, &posting_list), doc_right(query.get_left(), current, &posting_list)),
        "OR" => cmp::min(doc_right(query.get_right(), current, &posting_list), doc_right(query.get_left(), current, &posting_list)),
        _ => -1 as i32
    }
}

pub fn doc_left(query: Query, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if query.is_edge() {
        return prev_doc(query.term, current, &posting_list);
    }

    return match query.term.as_str() {
        "AND" => cmp::min(doc_left(query.get_right(), current, &posting_list), doc_left(query.get_left(), current, &posting_list)),
        "OR" => cmp::max(doc_left(query.get_right(), current, &posting_list), doc_left(query.get_left(), current, &posting_list)),
        _ => -1 as i32
    }
}

pub fn doc_right_not(query: Query, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if docid(current) == INF {
        return INF;
    }
    let mut u: i32 = docid(current);
    let mut v: i32 = next_doc(query.clone(), Posting::new(u, 1), &posting_list);
    while v == u + 1 {
        u = v;
        v = next_doc(query.clone(), Posting::new(u, 1), &posting_list);
    }

    return u + 1;
}