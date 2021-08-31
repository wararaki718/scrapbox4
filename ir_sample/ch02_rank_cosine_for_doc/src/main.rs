mod normalize;
mod posting_list;
mod tfidf_vectorizer;
mod rank_cosine;

use normalize::normalize;
use posting_list::get_posting_list_positional_index;
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
    for doc in docs {
        norm_docs.push(normalize(String::from(doc)));
    }
    let mut vectorizer = TfidfVectorizer::new();
    vectorizer.fit(&norm_docs);

    let dvecs = vectorizer.transform(&norm_docs);
    let qvecs = vectorizer.transform(&query);
    
    let pl = get_posting_list_positional_index(&norm_docs);
    let k: usize = 5 as usize;
    
    let keywords= query[0].split(" ").collect::<Vec<&str>>();
    let terms = keywords.iter().map(|x| x.to_string()).collect();
    let results = rank_cosine(qvecs[0].to_vec(), &terms, dvecs, &pl, k);
    for (i, result) in results.iter().enumerate() {
        println!("rank {}: docid={}, score={}", i+1, result.docid, result.score);
    }

    println!("DONE");
}
