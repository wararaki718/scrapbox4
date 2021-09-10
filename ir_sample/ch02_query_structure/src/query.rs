#[derive(Debug)]
pub struct Query {
    pub term: String,
    pub right: Box<Option<Query>>,
    pub left: Box<Option<Query>>
}


impl Query {
    pub fn new(term: String, right: Option<Query>, left: Option<Query>) -> Self {
        Self {
            term: term,
            right: Box::new(right),
            left: Box::new(left)
        }
    }
}
