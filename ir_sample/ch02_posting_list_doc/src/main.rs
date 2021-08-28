mod normalize;
mod operations;
mod posting_list;

use normalize::normalize;
use operations::{docid, offset};
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

    let pl = get_posting_list(&norm_docs);
    for (key, value) in &pl {
        println!("{} {:?}", key, value);
    }

    let position: i32 = 5;
    let did = docid(position, &pl);
    let off = offset(position, &pl);
    println!("docid({}) : {}", position, did);
    println!("offset({}): {}", position, off);
    println!("DONE");
}
