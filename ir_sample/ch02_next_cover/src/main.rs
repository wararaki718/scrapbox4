mod normalize;
mod next_cover;

use normalize::normalize;
use next_cover::next_cover;


fn main() {
    let docs = vec![
        "Do you quarrel, sir?",
        "Quarrel sir! no, sir!",
        "If you do, sir, I am for you: I serve as good a man as you.",
        "No better.",
        "Well, sir."
    ];
    let query = vec![
        "quarrel sir".to_string()
    ];
    let mut norm_docs = Vec::new();
    println!("documents:");
    for (i, doc) in docs.iter().enumerate() {
        norm_docs.push(normalize(doc.to_string()));
        println!("docid={}: {}", i+1, doc);
    }
    println!("");
    println!("DONE");
}
