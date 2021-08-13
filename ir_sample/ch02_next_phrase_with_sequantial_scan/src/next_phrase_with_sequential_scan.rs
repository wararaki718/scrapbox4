use std::collections::HashMap;
use std::sync::Mutex;
use once_cell::sync::Lazy;

static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;

static C_T_NEXT: Lazy<Mutex<HashMap<String, usize>>> = Lazy::new(||Mutex::new(HashMap::new()));
static C_T_PREV: Lazy<Mutex<HashMap<String, usize>>> = Lazy::new(||Mutex::new(HashMap::new()));


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

    let mut c_t: usize = 1;
    if C_T_NEXT.lock().unwrap().contains_key(&term) {
        c_t = match C_T_NEXT.lock().unwrap().get_mut(&term) {
            Some(c) => *c,
            None => 1
        }
    }
    if posting_index == NEG_INF {
        C_T_NEXT.lock().unwrap().remove(&term);
        C_T_NEXT.lock().unwrap().insert((&term).to_string(), 1);
        return first(term, &posting_list);
    }

    let indices = &posting_list[&term];
    if c_t > 1 || indices[c_t-1] > posting_index {
        c_t = 1;
    }
    while indices[c_t] <= posting_index {
        c_t += 1;
    }
    C_T_NEXT.lock().unwrap().remove(&term);
    C_T_NEXT.lock().unwrap().insert((&term).to_string(), c_t);
    return indices[c_t];
}

fn prev(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_index == NEG_INF {
        return NEG_INF;
    }

    let indices = &posting_list[&term];
    let l_t: usize = indices.len()-1;
    let mut c_t: usize = l_t;
    if C_T_PREV.lock().unwrap().contains_key(&term) {
        c_t = match C_T_PREV.lock().unwrap().get_mut(&term) {
            Some(c) => *c,
            None => l_t
        }
    }
    if posting_index == INF {
        C_T_PREV.lock().unwrap().remove(&term);
        C_T_PREV.lock().unwrap().insert((&term).to_string(), l_t);
        return last(term, &posting_list);
    }

    if c_t < l_t || indices[c_t-1] < posting_index {
        c_t = l_t;
    }
    while indices[c_t] >= posting_index {
        c_t -= 1;
    }
    C_T_PREV.lock().unwrap().remove(&term);
    C_T_PREV.lock().unwrap().insert((&term).to_string(), c_t);
    return indices[c_t];
}

pub fn next_phrase(terms: Vec<String>, position: i32, posting_list: &HashMap<String, Vec<i32>>) -> (i32, i32) {
    let mut v = position;
    for i in 0..terms.len() {
        let tv = &terms[i];
        v = next(tv.to_string(), v, &posting_list);
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