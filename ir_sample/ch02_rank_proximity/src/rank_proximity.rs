use std::collections::HashMap;

use crate::position::Position;
use crate::next_cover::next_cover;
use crate::operations::docid;
use crate::result::Result;

static INF: i32 = i32::MAX;


pub fn rank_proximity(terms: String, k: usize, posting_list: &HashMap<String, Vec<Position>>) -> Vec<Result> {
    let (mut u, mut v) = next_cover((&terms).to_string(), INF, &posting_list);
    let mut d = docid(u, &posting_list);

    let mut score: f32 = 0.0;
    let mut results: Vec<Result> = Vec::new();
    while u < INF {
        let u_docid = docid(u, &posting_list);
        if d < u_docid {
            results.push(Result::new(d, score));
            d = u_docid;
            score = 0.0;
        }
        score += 1.0/((v-u+1) as f32);
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