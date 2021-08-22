mod normalize;
mod tfidf_vectorizer;

use normalize::normalize;
use tfidf_vectorizer::TfidfVectorizer;

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
    for doc in &docs {
        norm_docs.push(normalize(doc.to_string()));
    }
    
    let mut vectorizer = TfidfVectorizer::new();
    vectorizer.fit(&norm_docs);
    println!("{:?}", vectorizer.feature_names());

    let vecs = vectorizer.transform(&norm_docs);
    for vec in vecs {
        println!("{:?}", vec);
    }

    println!("");
    let qvecs = vectorizer.transform(&query);
    for vec in qvecs {
        println!("{:?}", vec);
    }
    
    println!("DONE");
}
