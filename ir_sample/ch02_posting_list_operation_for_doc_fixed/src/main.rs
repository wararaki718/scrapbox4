mod doc_operations;
mod normalize;
mod operations;
mod posting;
mod posting_list;

use doc_operations::{first_doc, last_doc, next_doc, prev_doc};
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

    // sample data
    let position = Posting::new(2, 3);
    let term = "sir";

    // operations
    println!("operations");
    let did = docid(position);
    let off = offset(position);
    println!("docid({:?}) : {:?}", position, did);
    println!("offset({:?}): {:?}", position, off);

    let fdoc = first(String::from(term), &pl);
    let ldoc = last(String::from(term), &pl);
    let ndoc = next(String::from(term), position, &pl);
    let pdoc = prev(String::from(term), position, &pl);
    println!("first({})  : {:?}", term, fdoc);
    println!("last({})   : {:?}", term, ldoc);
    println!("next({}:{:?}): {:?}", term, position, ndoc);
    println!("prev({}:{:?}): {:?}", term, position, pdoc);
    println!("");

    println!("operations for documents");
    let fdoc2 = first_doc(String::from(term), &pl);
    let ldoc2 = last_doc(String::from(term), &pl);
    let ndoc2 = next_doc(String::from(term), position, &pl);
    let pdoc2 = prev_doc(String::from(term), position, &pl);
    println!("first_doc({})  : {:?}", term, fdoc2);
    println!("last_doc({})   : {:?}", term, ldoc2);
    println!("next_doc({}:{:?}): {:?}", term, position, ndoc2);
    println!("prev_doc({}:{:?}): {:?}", term, position, pdoc2);

    println!("DONE");
}
