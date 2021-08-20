mod normalize;
mod tfidf;

use normalize::normalize;
use tfidf::vectorize_tfidf;

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
    
    let vecs = vectorize_tfidf(&norm_docs);
    for v in vecs {
        println!("{:?}", v);
    }
    
    println!("DONE");
}
