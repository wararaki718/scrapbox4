#[derive(Clone, Copy, Debug)]
pub struct Posting {
    pub docid: i32,
    pub offset: i32,
}

impl Posting {
    pub fn new(docid: i32, offset: i32) -> Self {
        Self {
            docid,
            offset
        }
    }
}
