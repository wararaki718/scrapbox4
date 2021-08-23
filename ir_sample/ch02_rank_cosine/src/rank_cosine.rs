#[derive(Clone)]
pub struct Result {
    pub docid: i32,
    pub score: f32
}

fn cosine_similarity(x: Vec<f32>, y: Vec<f32>) -> f32 {
    let xy: f32 = x.iter().zip(y.iter()).map(|(x_, y_)| x_*y_).sum();
    let _x: f32 = x.iter().map(|x_| x_*x_).sum::<f32>().sqrt();
    let _y: f32 = y.iter().map(|y_| y_*y_).sum::<f32>().sqrt();
    let sim: f32 = xy / _x / _y;
    return sim;
}

pub fn rank_cosine(x_term: Vec<f32>, x_docs: Vec<Vec<f32>>, k: usize) -> Vec<Result> {
    let mut results: Vec<Result> = Vec::new();

    for (i, x_doc) in x_docs.iter().enumerate() {
        let score = cosine_similarity(x_term.to_vec(), x_doc.to_vec());
        results.push(Result{docid: (i+1) as i32, score: score});
    }

    results.sort_by(|x, y| y.score.partial_cmp(&x.score).unwrap());
    if let Some(r) = results.get(0..k) {
        return r.to_vec();
    }
    return results;
}