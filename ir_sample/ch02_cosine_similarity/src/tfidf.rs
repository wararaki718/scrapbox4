use std::collections::{HashMap, HashSet};


pub fn vectorize_tfidf(docs: &Vec<String>) -> Vec<Vec<f32>> {
    let mut f_t: HashMap<String, i32> = HashMap::new();
    
    for doc in docs {
        let terms: HashSet<&str> = doc.split(" ").into_iter().collect();
        for term in terms {
            if !f_t.contains_key(&term.to_string()) {
                f_t.insert(term.to_string(), 0 as i32);
            }
            if let Some(f) = f_t.get_mut(&term.to_string()) {
                *f += 1 as i32;
            }
        }
    }

    let mut tfidf: Vec<Vec<f32>> = Vec::new();
    for doc in docs {
        let terms = doc.split(" ");
        let mut f_t_d: HashMap<String, i32> = HashMap::new();
        for term in terms {
            if !f_t_d.contains_key(&term.to_string()) {
                f_t_d.insert(term.to_string(), 0 as i32);
            }
            if let Some(f) = f_t_d.get_mut(&term.to_string()) {
                *f += 1 as i32;
            }
        }

        let n = docs.len() as f32;
        let e = 2.0;
        let mut v: Vec<f32> = Vec::new();
        for (term, f) in &f_t {
            if f_t_d.contains_key(term) {
                if let Some(f_td) = f_t_d.get_mut(term) {
                    let tf = (*f_td as f32).log(e) + 1.0;
                    let idf = (n / *f as f32).log(e);
                    v.push(tf*idf);
                } else {
                    v.push(0 as f32);
                }
            } else {
                v.push(0 as f32);
            }
        }

        tfidf.push(v);
    }

    return tfidf;
}
