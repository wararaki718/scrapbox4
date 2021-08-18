struct User {
    id: i32,
    name: String,
    admin: bool
}

impl User {
    pub fn new(id: i32, name: String) -> Self {
        Self {
            id,
            name,
            admin: false
        }
    }
}


fn main() {
    let user = User::new(1, "name".to_string());
    println!("{}: {}: {}", user.id, user.name, user.admin);
    println!("DONE");
}
