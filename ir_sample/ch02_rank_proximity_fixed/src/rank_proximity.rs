use std::collections::HashMap;

use crate::posting::Posting;
use crate::result::Result;
use crate::operations::{docid, offset};
use crate::next_cover::next_cover;

static INF: i32 = i32::MAX;
// static NEG_INF: i32 = i32::MIN;


pub fn rank_proximity(terms: String, k: usize, posting_list: &HashMap<String, Vec<Posting>>) -> Vec<Result> {
    let mut results: Vec<Result> = Vec::new();
    let (mut u, mut v) = next_cover((&terms).to_string(), Posting::new(INF, INF), &posting_list);
    // println!("{:?}", u);
    // println!("{:?}", v);

    let mut d = docid(u);
    let mut score: f32 = 0.0;
    while docid(u) < INF && offset(u) < INF {
        if d < docid(u) {
            results.push(Result::new(d, score));
            d = docid(u);
            score = 0.0;
        }
        score += 1.0 / (offset(v)-offset(u)+1 as i32) as f32;
        let tmp = next_cover((&terms).to_string(), u, &posting_list);
        u = tmp.0;
        v = tmp.1;
    }

    if d < INF {
        results.push(Result::new(d, score));
    }
    results.sort_by(|x, y| y.score.partial_cmp(&x.score).unwrap());
    if let Some(r) = results.get(0..k) {
        return r.to_vec();
    }
    return results;
}
