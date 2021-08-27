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

pub fn next_cover(terms: String, position: i32, posting_list: &HashMap<String, Vec<i32>>) -> (i32, i32) {
    let v: i32 = terms.split(" ").map(|x| next(String::from(x), position, &posting_list)).max().map_or(INF, |x| x);
    if v == INF {
        return (INF, INF);
    }
    let u: i32 = terms.split(" ").map(|x| prev(String::from(x), v+1 as i32, &posting_list)).min().map_or(NEG_INF, |x| x);
    return (u, v);
}
