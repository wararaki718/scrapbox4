mod normalize;
mod posting_list;

use normalize::normalize;
use posting_list::get_posting_list_positional_index;

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
    let pl_pos = get_posting_list_positional_index(&norm_docs);

    // check
    let term = "quarrel";
    println!("term={}", term);
    println!("positional index: {:?}", pl_pos[term]);
    println!("DONE");
}
