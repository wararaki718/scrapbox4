use std::collections::{HashMap, HashSet};


pub struct TfidfVectorizer {
    n: i32,
    f_t: HashMap<String, i32>
}

impl TfidfVectorizer {
    pub fn new() -> Self {
        Self {
            n: 0 as i32,
            f_t: HashMap::new()
        }
    }

    pub fn feature_names(self: &Self) -> Vec<String> {
        let mut names: Vec<String> = Vec::new();
        for key in self.f_t.keys() {
            names.push(key.to_string());
        }
        return names;
    }

    pub fn fit(&mut self, docs: &Vec<String>) {
        self.n = docs.len() as i32;
        for doc in docs {
            let terms: HashSet<&str> = doc.split(" ").into_iter().collect();
            for term in terms {
                if !self.f_t.contains_key(&term.to_string()) {
                    self.f_t.insert(term.to_string(), 0 as i32);
                }
                if let Some(f) = self.f_t.get_mut(&term.to_string()) {
                    *f += 1 as i32;
                }
            }
        }
    }

    fn normalize(self: &Self, vecs: Vec<Vec<f32>>) -> Vec<Vec<f32>> {
        let mut x_norm: Vec<Vec<f32>> = Vec::new();
        for vec in vecs {
            let x_ = vec.iter().map(|x| x*x).sum::<f32>().sqrt();
            x_norm.push(vec.iter().map(|x| x / x_).collect());
        }
        return x_norm;
    }

    pub fn transform(self: &Self, docs: &Vec<String>) -> Vec<Vec<f32>> {
        let mut x_tfidf: Vec<Vec<f32>> = Vec::new();
        for doc in docs {
            let mut f_t_d: HashMap<String, i32> = HashMap::new();
            for term in doc.split(" ") {
                if !f_t_d.contains_key(&term.to_string()) {
                    f_t_d.insert(term.to_string(), 0 as i32);
                }
                if let Some(f) = f_t_d.get_mut(&term.to_string()) {
                    *f += 1 as i32;
                }
            }
    
            let e = 2.0;
            let mut v: Vec<f32> = Vec::new();
            for (term, f) in &self.f_t {
                let mut x = 0 as f32;
                if f_t_d.contains_key(term) {
                    if let Some(f_td) = f_t_d.get_mut(term) {
                        let tf = (*f_td as f32).log(e) + 1.0;
                        let idf = (self.n as f32 / *f as f32).log(e);
                        x = tf*idf;
                    }
                }
                v.push(x);
            }
            x_tfidf.push(v);
        }
    
        return self.normalize(x_tfidf);
    }
}
