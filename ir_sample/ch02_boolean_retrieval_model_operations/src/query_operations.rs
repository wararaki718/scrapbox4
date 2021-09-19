use std::collections::HashMap;
use std::cmp;

use crate::operations::docid;
use crate::doc_operations::{next_doc, prev_doc};
use crate::posting::Posting;
use crate::query::Query;

static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;

pub fn doc_right(query: Query, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if query.is_edge() {
        if query.is_not {
            return doc_right_not(query, current, &posting_list);
        }
        return next_doc(query.term, current, &posting_list);
    }

    if query.is_not {
        let mut q_right = query.get_right();
        let mut q_left = query.get_left();
        q_right.is_not = !q_right.is_not;
        q_left.is_not = !q_left.is_not;
        return match query.term.as_str() {
            "AND" => cmp::min(doc_right(q_right, current, &posting_list), doc_right(q_left, current, &posting_list)),
            "OR" => cmp::max(doc_right(q_right, current, &posting_list), doc_right(q_left, current, &posting_list)),
            _ => -1 as i32
        }
    }

    return match query.term.as_str() {
        "AND" => cmp::max(doc_right(query.get_right(), current, &posting_list), doc_right(query.get_left(), current, &posting_list)),
        "OR" => cmp::min(doc_right(query.get_right(), current, &posting_list), doc_right(query.get_left(), current, &posting_list)),
        _ => -1 as i32
    }
}

pub fn doc_left(query: Query, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if query.is_edge() {
        if query.is_not {
            return doc_left_not(query, current, &posting_list);
        }
        return prev_doc(query.term, current, &posting_list);
    }

    if query.is_not {
        let mut q_right = query.get_right();
        let mut q_left = query.get_left();
        q_right.is_not = !q_right.is_not;
        q_left.is_not = !q_left.is_not;
        return match query.term.as_str() {
            "AND" => cmp::max(doc_left(q_right, current, &posting_list), doc_left(q_left, current, &posting_list)),
            "OR" => cmp::min(doc_left(q_right, current, &posting_list), doc_left(q_left, current, &posting_list)),
            _ => -1 as i32
        }
    }

    return match query.term.as_str() {
        "AND" => cmp::min(doc_left(query.get_right(), current, &posting_list), doc_left(query.get_left(), current, &posting_list)),
        "OR" => cmp::max(doc_left(query.get_right(), current, &posting_list), doc_left(query.get_left(), current, &posting_list)),
        _ => -1 as i32
    }
}

fn doc_right_not(query: Query, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if docid(current) == INF {
        return INF;
    }
    let term = query.term;
    let mut u: i32 = docid(current);
    let mut v: i32 = next_doc(term.clone(), Posting::new(u, NEG_INF), &posting_list);
    while v < INF && u < INF && v == u + 1 {
        u = v;
        v = next_doc(term.clone(), Posting::new(u, NEG_INF), &posting_list);
    }

    return u + 1;
}


fn doc_left_not(query: Query, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    if docid(current) == NEG_INF {
        return NEG_INF;
    }
    
    let term = query.term;
    let mut u: i32 = docid(current);
    let mut v: i32 = prev_doc(term.clone(), Posting::new(u, INF), &posting_list);
    while v > NEG_INF && u > NEG_INF && v == u - 1 {
        u = v;
        v = prev_doc(term.clone(), Posting::new(u, INF), &posting_list);
    }

    return u;
}
