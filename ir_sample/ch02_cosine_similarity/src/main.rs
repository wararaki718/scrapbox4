mod normalize;
mod tfidf;
mod similarity;

use normalize::normalize;
use tfidf::vectorize_tfidf;
use similarity::cosine_similarity;


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
    for v in vecs.to_vec() {
        println!("{:?}", v);
    }

    let sim = cosine_similarity(vecs[0].to_vec(), vecs[1].to_vec());
    println!("{}", sim);
    let sim2 = cosine_similarity(vecs[3].to_vec(), vecs[4].to_vec());
    println!("{}", sim2);
    
    println!("DONE");
}
