#[derive(Debug)]
pub struct Document {
    pub id: i32,
    pub offset: i32,
}

impl Document {
    pub fn new(id: i32, offset: i32) -> Document {
        Self {
            id: id,
            offset: offset
        }
    }
}
