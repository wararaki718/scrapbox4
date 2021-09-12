#[derive(Debug, Clone)]
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

    pub fn is_edge(&self) -> bool {
        return !(self.right.is_some() && self.left.is_some());
    }

    pub fn get_right(&self) -> Self {
        let result = (*self.right).as_ref().unwrap();
        return result.clone();
    }

    pub fn get_left(&self) -> Self {
        let result = (*self.left).as_ref().unwrap();
        return result.clone();
    }
}
