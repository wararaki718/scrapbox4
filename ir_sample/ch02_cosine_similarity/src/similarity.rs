pub fn cosine_similarity(x: Vec<f32>, y: Vec<f32>) -> f32 {
    let xy: f32 = x.iter().zip(y.iter()).map(|(x_, y_)| x_*y_).sum();
    let _x: f32 = x.iter().map(|x_| x_*x_).sum::<f32>().sqrt();
    let _y: f32 = y.iter().map(|y_| y_*y_).sum::<f32>().sqrt();
    let sim: f32 = xy / _x / _y;
    return sim;
}
