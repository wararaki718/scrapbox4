use std::collections::HashMap;
use crate::operations::{docid, offset, next, prev};
use crate::posting::Posting;

static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


pub fn next_cover(terms: String, position: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> (Posting, Posting) {
    let v: Posting = terms.split(" ").map(|x| next(String::from(x), position, &posting_list)).max().map_or(Posting::new(NEG_INF, NEG_INF), |x| x);
    if docid(v) == INF ||  offset(v) == INF {
        return (Posting::new(INF, INF), Posting::new(INF, INF));
    }
    let u: Posting = terms.split(" ").map(|x| prev(String::from(x), Posting::new(docid(v), offset(v)+1), &posting_list)).min().map_or(Posting::new(INF, INF), |x| x);

    // println!("u={:?}, v={:?}", u, v);
    if docid(u) == docid(v) {
        return (u, v);
    }
    return next_cover(terms, v, &posting_list);
}
