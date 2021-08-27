mod normalize;
mod next_cover;
mod posting_list;

use normalize::normalize;
use next_cover::next_cover;
use posting_list::{get_posting_list, get_posting_list_positional_index};


fn main() {
    let docs = vec![
        "Do you quarrel, sir?",
        "Quarrel sir! no, sir!",
        "If you do, sir, I am for you: I serve as good a man as you.",
        "No better.",
        "Well, sir."
    ];
    /*
    let query = vec![
        String::from("quarrel sir")
    ];
    */

    let mut norm_docs = Vec::new();
    for doc in docs {
        norm_docs.push(normalize(String::from(doc)));
    }

    // create posting list
    //let pl_pos = get_posting_list_positional_index(&norm_docs);
    let pl = get_posting_list(&norm_docs);
    /*
    for key in pl.keys() {
        println!("{}: {:?}", key, pl[key]);
    }
    */
    let result = next_cover(String::from("quarrel sir"), 0, &pl);
    println!("{:?}", result);
    println!("DONE");
}
