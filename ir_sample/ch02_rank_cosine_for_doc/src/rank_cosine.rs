use std::collections::HashMap;

use ch02_rank_cosine_for_doc::position::Position;
use ch02_rank_cosine_for_doc::result::Result;


static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


fn cosine_similarity(x: Vec<f32>, y: Vec<f32>) -> f32 {
    let xy: f32 = x.iter().zip(y.iter()).map(|(x_, y_)| x_*y_).sum();
    let _x: f32 = x.iter().map(|x_| x_*x_).sum::<f32>().sqrt();
    let _y: f32 = y.iter().map(|y_| y_*y_).sum::<f32>().sqrt();
    let sim: f32 = xy / _x / _y;
    return sim;
}


pub fn first_doc(term: String, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    if posting_list.contains_key(&term) {
        if let Some(doc) = &posting_list[&term].first() {
            return doc.d;
        }
    }
    return NEG_INF;
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


fn min_next_doc(terms: &Vec<String>, docid: i32, posting_list: &HashMap<String, Vec<Position>>) -> i32 {
    let first_term = String::from(&terms[0]);
    let mut next_docid: i32 = next_doc(first_term, docid, posting_list);
    for term in terms {
        let candidate_docid = next_doc(String::from(term), docid, posting_list);
        if candidate_docid < next_docid {
            next_docid = candidate_docid;
        }
    }

    return next_docid;
}

pub fn rank_cosine(x_term: Vec<f32>, terms: &Vec<String>, x_docs: Vec<Vec<f32>>, posting_list: &HashMap<String, Vec<Position>>, k: usize) -> Vec<Result> {
    let mut results: Vec<Result> = Vec::new();
    let mut docid: i32 = min_next_doc(&terms, NEG_INF, &posting_list);

    while docid < INF {
        let x_doc = &x_docs[(docid-1) as usize];
        let score = cosine_similarity(x_term.to_vec(), x_doc.to_vec());
        results.push(Result{docid: docid, score: score});
        docid = min_next_doc(&terms, docid, &posting_list);
    }

    results.sort_by(|x, y| y.score.partial_cmp(&x.score).unwrap());
    if let Some(r) = results.get(0..k) {
        return r.to_vec();
    }
    return results;
}
