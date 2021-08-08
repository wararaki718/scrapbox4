use std::collections::HashMap;

fn get_posting_list() -> HashMap<String, Vec<i32>> {
    let v = vec![11, 22, 33];
    let v2 = vec![44, 55, 66];
    let v3 = vec![77, 88, 99];
    let mut posting_list = HashMap::new();
    posting_list.insert("first".to_string(), v);
    posting_list.insert("second".to_string(), v2);
    posting_list.insert("third".to_string(), v3);

    return posting_list;
}

fn first(term: String, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        return indices[0];
    }
    return -1;
}

fn last(term: String, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        let length = posting_list.len();
        return indices[length-1];
    }
    return -1;
}

fn next(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        let index = indices.binary_search(&posting_index).unwrap();
        if index+1 >= indices.len() {
            return -1;
        }
        return indices[index+1] as i32;
    }
    return -1;
}

fn prev(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        let index = indices.binary_search(&posting_index).unwrap();
        if index-1 >= 0 {
            return indices[index-1] as i32;
        }
    }
    return -1;
}

fn main() {
    let posting_list = get_posting_list();
    let result_first = first("first".to_string(), &posting_list);
    let result_last = last("first".to_string(), &posting_list);
    let result_next = next("first".to_string(), result_first, &posting_list);
    let result_prev = prev("first".to_string(), result_last, &posting_list);
    println!("first: {}", result_first);
    println!("last : {}", result_last);
    println!("next : {}", result_next);
    println!("prev : {}", result_prev);

    println!("DONE");
}
