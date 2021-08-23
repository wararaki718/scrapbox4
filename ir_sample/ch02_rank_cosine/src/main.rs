mod normalize;
mod tfidf_vectorizer;
mod rank_cosine;

use normalize::normalize;
use tfidf_vectorizer::TfidfVectorizer;
use rank_cosine::rank_cosine;

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
    
    let mut vectorizer = TfidfVectorizer::new();
    vectorizer.fit(&norm_docs);
    println!("vocabularies:");
    println!("{:?}", vectorizer.feature_names());
    println!("");

    println!("query:");
    println!("{:?}", query);
    println!("");

    let vecs = vectorizer.transform(&norm_docs);
    let qvecs = vectorizer.transform(&query);

    let k: usize = 5 as usize;
    let results = rank_cosine(qvecs[0].to_vec(), vecs, k);
    for (i, result) in results.iter().enumerate() {
        println!("rank {}: docid={}, score={}", i+1, result.docid, result.score);
    }
    
    println!("DONE");
}
