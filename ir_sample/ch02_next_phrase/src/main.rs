use std::collections::HashMap;


static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


fn get_posting_list() -> HashMap<String, Vec<i32>> {
    let v = vec![NEG_INF, 11, 22, 33, 66, INF];
    let v2 = vec![NEG_INF, 44, 55, 66, INF];
    let v3 = vec![NEG_INF, 77, 88, 99, INF];
    let mut posting_list = HashMap::new();
    posting_list.insert("first".to_string(), v);
    posting_list.insert("second".to_string(), v2);
    posting_list.insert("third".to_string(), v3);

    return posting_list;
}

fn next(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        println!("{}: {}", term, posting_index);
        let index = indices.binary_search(&posting_index);
        println!("{}", index.unwrap());
        if index.unwrap()+1 >= indices.len() {
            return -1;
        }
        return indices[index.unwrap()+1] as i32;
    }
    return -1;
}

fn prev(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        let index = indices.binary_search(&posting_index).unwrap();
        if index-1 >= 0 as usize {
            return indices[index-1] as i32;
        }
    }
    return -1;
}

fn next_phrase(terms: Vec<String>, position: i32, posting_list: &HashMap<String, Vec<i32>>) -> (i32, i32) {
    let mut v = position;
    for i in 0..terms.len() {
        let tv = &terms[i];
        v = next(tv.to_string(), v, &posting_list);
    }
    if v == INF {
        return (INF, INF);
    }

    let mut u = v;
    for i in (0..terms.len()).rev() {
        let tu = &terms[i];
        u = prev(tu.to_string(), u, &posting_list);
    }

    if (v-u) as usize == terms.len()-1 {
        return (u, v);
    } else {
        return next_phrase(terms, u, &posting_list)
    }
}

fn main() {
    let posting_list = get_posting_list();
    /*
    let result_first = first("first".to_string(), &posting_list);
    let result_last = last("first".to_string(), &posting_list);
    let result_next = next("first".to_string(), result_first, &posting_list);
    let result_prev = prev("first".to_string(), result_last, &posting_list);
    println!("first: {}", result_first);
    println!("last : {}", result_last);
    println!("next : {}", result_next);
    println!("prev : {}", result_prev);
    */
    let terms = vec!["first".to_string(), "second".to_string()];
    let position = NEG_INF;
    let result = next_phrase(terms, position, &posting_list);
    println!("{:?}", result);
    println!("DONE");
}
