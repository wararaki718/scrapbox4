#[derive(Debug, Clone)]
pub struct User {
    pub id: i32,
    pub name: String,
}


impl User {
    pub fn new(id: i32, name: String) -> Self {
        Self {
            id: id,
            name: name
        }
    }
}
