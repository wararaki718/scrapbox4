use std::collections::HashMap;

fn get_posting_list() -> HashMap<String, Vec<i32>> {
    let v = vec![1, 2, 3];
    let v2 = vec![4, 5, 6];
    let v3 = vec![7, 8, 9];
    let mut posting_list = HashMap::new();
    posting_list.insert("first".to_string(), v);
    posting_list.insert("second".to_string(), v2);
    posting_list.insert("third".to_string(), v3);

    return posting_list;
}

fn first(term: String, posting_list: HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        return indices[0];
    }
    return -1;
}

fn main() {
    let posting_list = get_posting_list();
    let result = first("first".to_string(), posting_list);
    println!("first: {}", result);

    println!("DONE");
}
