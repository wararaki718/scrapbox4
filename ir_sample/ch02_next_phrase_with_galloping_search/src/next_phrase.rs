use std::collections::HashMap;


static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


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

    let indices = &posting_list[&term];
    for index in indices {
        if posting_index < *index {
            return *index;
        }
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

    let indices = &posting_list[&term];
    for index in indices.iter().rev() {
        if posting_index > *index {
            return *index;
        }
    }
    return NEG_INF;
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