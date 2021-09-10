mod normalize;
mod operations;
mod posting;
mod posting_list;
mod result;
mod next_cover;
mod rank_proximity;

use next_cover::next_cover;
use normalize::normalize;
use posting::Posting;
use posting_list::get_posting_list;
use rank_proximity::rank_proximity;


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
        if key == "sir" || key == "you" {
            println!("{}: {:?}", key, value);
        }
    }
    println!("");

    println!("next cover:");
    let terms = "you sir";
    let position = Posting::new(1, 1);
    let result = next_cover(String::from(terms), position, &pl);
    println!("result: {:?}", result);
    println!("");

    println!("rank proximity:");
    let results = rank_proximity(String::from(terms), 3, &pl);
    for r in results {
        println!("{:?}", r);
    }
    println!("");

    println!("DONE");
}
