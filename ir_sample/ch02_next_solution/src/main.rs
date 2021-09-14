mod doc_operations;
mod normalize;
mod operations;
mod posting;
mod posting_list;
mod query;
mod query_operations;
mod next_solution;

use normalize::normalize;
use posting::Posting;
use posting_list::get_posting_list;
use query::Query;
use next_solution::{next_solution, next_solution_all};


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
    let position = Posting::new(i32::MIN, i32::MIN);

    let q1 = Query::new(String::from("quarrel"), None, None);
    let q2 = Query::new(String::from("sir"), None, None);
    let q3 = Query::new(String::from("you"), None, None);

    let q4 = Query::new(String::from("OR"), Some(q1), Some(q2));
    let query = Query::new(String::from("AND"), Some(q4), Some(q3));

    let result = next_solution(query.clone(), position, &pl);
    println!("get one:");
    println!("result = {:?}", result);
    println!("");
    let results = next_solution_all(query.clone(), &pl);
    println!("get all:");
    for res in results {
        println!("{:?}", res);
    }
    println!("");
    println!("DONE");
}
