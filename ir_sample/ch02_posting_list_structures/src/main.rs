mod normalize;
mod posting_list;

use normalize::normalize;
use posting_list::{get_posting_list_docid_index, get_posting_list_frequency_index, get_posting_list_scheme_independent_index};

fn main() {
    let docs = vec![
        "Do you quarrel, sir?",
        "Quarrel sir! no, sir!",
        "If you do, sir, I am for you: I serve as good a man as you.",
        "No better.",
        "Well, sir."
    ];
    let mut norm_docs = Vec::new();
    for doc in &docs {
        norm_docs.push(normalize(doc.to_string()));
    }
    
    // create posting list
    let pl_docid = get_posting_list_docid_index(&norm_docs);
    let pl_freq = get_posting_list_frequency_index(&norm_docs);
    let pl_si = get_posting_list_scheme_independent_index(&norm_docs);

    // check
    let term = "quarrel";
    println!("term={}", term);
    println!("docid index             : {:?}", pl_docid[term]);
    println!("frequency index         : {:?}", pl_freq[term]);
    println!("scheme-independent index: {:?}", pl_si[term]);
    println!("DONE");
}
