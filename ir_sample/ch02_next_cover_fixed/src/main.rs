mod normalize;
mod operations;
mod posting;
mod posting_list;
mod next_cover;

use next_cover::next_cover;
use normalize::normalize;
use operations::{docid, offset, first, last, next, prev};
use posting::Posting;
use posting_list::get_posting_list;

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

    println!("operations");
    let position = Posting::new(1, 1);
    let did = docid(position);
    let off = offset(position);
    println!("docid({:?}) : {:?}", position, did);
    println!("offset({:?}): {:?}", position, off);

    let term = "sir";
    let fdoc = first(String::from(term), &pl);
    let ldoc = last(String::from(term), &pl);
    let ndoc = next(String::from(term), position, &pl);
    let pdoc = prev(String::from(term), position, &pl);
    println!("first({})  : {:?}", term, fdoc);
    println!("last({})   : {:?}", term, ldoc);
    println!("next({}:{:?}): {:?}", term, position, ndoc);
    println!("prev({}:{:?}): {:?}", term, position, pdoc);
    println!("");

    println!("next cover:");
    let terms = "quarrel sir";
    let result = next_cover(String::from(terms), position, &pl);
    println!("result: {:?}", result);
    println!("DONE");
}
