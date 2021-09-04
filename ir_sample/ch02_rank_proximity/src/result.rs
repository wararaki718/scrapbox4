#[derive(Debug, Clone)]
pub struct Result {
    pub docid: i32,
    pub score: f32
}

impl Result {
    pub fn new(docid: i32, score: f32) -> Self {
        Self {
            docid, score
        }
    }
}
