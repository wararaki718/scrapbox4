pub struct Sample {
    pub name: String,
}

impl Sample {
    pub fn new(name: String) -> Sample {
        Self {
            name: name
        }
    }
}