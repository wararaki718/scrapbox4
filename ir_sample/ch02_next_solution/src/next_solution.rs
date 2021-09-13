use std::collections::HashMap;

use crate::operations::docid;
use crate::query_operations::{doc_right, doc_left};
use crate::posting::Posting;
use crate::query::Query;

static INF: i32 = i32::MAX;


pub fn next_solution(query: Query, position: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> i32 {
    let v = doc_right(query.clone(), position, &posting_list);
    if v == Posting::new(INF, INF) {
        return INF;
    }

    let u = doc_left(query.clone(), Posting::new(docid(v)+1, 1), &posting_list);
    if docid(u) == docid(v) {
        return docid(u);
    }

    return next_solution(query, v, &posting_list);
}