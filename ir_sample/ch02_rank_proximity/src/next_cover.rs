use std::collections::HashMap;
use crate::operations::{docid, next, prev};
use crate::position::Position;

static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


pub fn next_cover(terms: String, position: i32, posting_list: &HashMap<String, Vec<Position>>) -> (i32, i32) {
    let v: i32 = terms.split(" ").map(|x| next(String::from(x), position, &posting_list)).max().map_or(INF, |x| x);
    if v == INF {
        return (INF, INF);
    }
    let u: i32 = terms.split(" ").map(|x| prev(String::from(x), v+1 as i32, &posting_list)).min().map_or(NEG_INF, |x| x);
    if docid(u, &posting_list) == docid(v, &posting_list) {
        return (u, v);
    }
    return next_cover(terms, u, &posting_list);
}
