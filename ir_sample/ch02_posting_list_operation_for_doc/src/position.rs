#[derive(Debug)]
pub struct Position {
    pub d: i32,
    pub f_td: i32,
    pub p: Vec<i32>
}

impl Position {
    pub fn new(d: i32, f_td: i32, p: Vec<i32>) -> Self {
        Self {
            d, f_td, p
        }
    }
}
