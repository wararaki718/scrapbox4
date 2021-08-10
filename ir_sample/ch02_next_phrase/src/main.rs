use std::collections::HashMap;


static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


fn get_posting_list() -> HashMap<String, Vec<i32>> {
    let v = vec![NEG_INF, 11, 22, 33, 66, INF];
    let v2 = vec![NEG_INF, 8, 9, 12, INF];
    let v3 = vec![NEG_INF, 77, 88, 99, INF];
    let mut posting_list = HashMap::new();
    posting_list.insert("first".to_string(), v);
    posting_list.insert("second".to_string(), v2);
    posting_list.insert("third".to_string(), v3);

    return posting_list;
}

fn first(term: String, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        return indices[1];
    }
    return NEG_INF;
}

fn last(term: String, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        let length = indices.len();
        return indices[length-2];
    }
    return INF;
}

fn next(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_index == INF {
        return INF;
    }
    if posting_index == NEG_INF {
        return first(term, &posting_list);
    }

    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        let index = indices.binary_search(&posting_index).unwrap_or(indices.len()-1);
        if index+1 >= indices.len() {
            return INF;
        }
        return indices[index+1] as i32;
    }
    return INF;
}

fn prev(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_index == NEG_INF {
        return NEG_INF;
    }
    if posting_index == INF {
        return last(term, &posting_list);
    }

    if posting_list.contains_key(&term) {
        let indices = &posting_list[&term];
        let index = indices.binary_search(&posting_index).unwrap_or(1 as usize);
        if index-1 >= 0 as usize {
            return indices[index-1] as i32;
        }
    }
    return NEG_INF;
}

fn next_phrase(terms: Vec<String>, position: i32, posting_list: &HashMap<String, Vec<i32>>) -> (i32, i32) {
    let mut v = position;
    for i in 0..terms.len() {
        let tv = &terms[i];
        v = next(tv.to_string(), v, &posting_list);
        println!("{}: {}", tv, v);
    }
    if v == INF {
        return (INF, INF);
    }

    let mut u = v;
    for i in (0..terms.len()-1).rev() {
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
