mod normalize;
mod next_cover;
mod result;
mod operations;
mod posting_list;
mod position;
mod rank_proximity;

use normalize::normalize;
use posting_list::get_posting_list_positional_index;
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

    let pl = get_posting_list_positional_index(&norm_docs);
    let result = rank_proximity(String::from("quarrel sir"), 3, &pl);
    println!("{:?}", result);
    println!("DONE");
}
