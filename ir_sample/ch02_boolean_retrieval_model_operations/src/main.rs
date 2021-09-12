mod doc_operations;
mod normalize;
mod operations;
mod posting;
mod posting_list;
mod query;
mod query_operations;

use normalize::normalize;
use posting::Posting;
use posting_list::get_posting_list;
use query::Query;
use query_operations::{doc_right, doc_left};


fn main() {
    let docs = vec![
        "Do you quarrel, sir?",
        "Quarrel sir! no, sir!",
        "If you do, sir, I am for you: I serve as good a man as you.",
        "No better.",
        "Well, sir."
    ];
    let mut norm_docs = Vec::new();
    for doc in docs {
        norm_docs.push(normalize(String::from(doc)));
    }
    
    // create posting list
    let pl = get_posting_list(&norm_docs);

    // check
    println!("posting list:");
    for (key, value) in &pl {
        println!("{}: {:?}", key, value);
    }
    println!("");

    // sample data
    let p_right = Posting::new(1, 1);
    let p_left = Posting::new(5, 20);

    let q1 = Query::new(String::from("quarrel"), None, None);
    let q2 = Query::new(String::from("sir"), None, None);
    let q3 = Query::new(String::from("you"), None, None);

    let q4 = Query::new(String::from("OR"), Some(q1), Some(q2));
    let q5 = Query::new(String::from("AND"), Some(q4), Some(q3));
    let q6 = q5.clone();

    let result_right = doc_right(q5, p_right, &pl);
    let result_left = doc_left(q6, p_left, &pl);
    println!("doc_right: docid = {}", result_right);
    println!("doc_left : docid = {}", result_left);
    println!("DONE");
}