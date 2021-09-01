use crate::user;


pub fn create_user(id: i32, name: String) -> user::User {
    return user::User::new(id, name);
}
