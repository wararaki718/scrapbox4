use std::collections::HashMap;

use crate::operations::docid;
use crate::query_operations::{doc_right, doc_left};
use crate::posting::Posting;
use crate::query::Query;

static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


pub fn next_solution(query: Query, position: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> Posting {
    let v = doc_right(query.clone(), position, &posting_list);
    if docid(v) == INF {
        return Posting::new(INF, INF);
    }

    let u = doc_left(query.clone(), Posting::new(docid(v)+1, 1), &posting_list);
    if docid(u) == docid(v) {
        return u;
    }

    return next_solution(query, v, &posting_list);
}


pub fn next_solution_all(query: Query, posting_list: &HashMap<String, Vec<Posting>>) -> Vec<Posting> {
    let mut u = Posting::new(NEG_INF, NEG_INF);
    let mut results: Vec<Posting> = Vec::new();
    while docid(u) < INF {
        u = next_solution(query.clone(), u, &posting_list);
        if docid(u) < INF {
            results.push(u);
        }
    }

    return results;
}
