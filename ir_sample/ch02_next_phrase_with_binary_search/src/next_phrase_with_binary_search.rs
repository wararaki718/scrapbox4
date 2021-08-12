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

fn binary_search_next(p_t: &Vec<i32>, low_: usize, high_: usize, current: i32) -> usize {
    let mut high = high_;
    let mut low = low_;
    while high - low > 1 {
        let mid: usize = (high+low)/2;
        if p_t[mid] <= current {
            low = mid;
        } else {
            high = mid;
        }
    }
    return high;
}

fn next(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_index == INF {
        return INF;
    }
    if posting_index == NEG_INF {
        return first(term, &posting_list);
    }

    let indices = &posting_list[&term];
    return indices[binary_search_next(indices, 1, indices.len()-1, posting_index)];
}


fn binary_search_prev(p_t: &Vec<i32>, low_: usize, high_: usize, current: i32) -> usize {
    let mut low = low_;
    let mut high = high_;
    while high - low > 1 {
        let mid: usize = (high+low) / 2;
        if p_t[mid] <= current {
            low = mid;
        } else {
            high = mid;
        }
    }
    return low;
}

fn prev(term: String, posting_index: i32, posting_list: &HashMap<String, Vec<i32>>) -> i32 {
    if posting_index == NEG_INF {
        return NEG_INF;
    }
    if posting_index == INF {
        return last(term, &posting_list);
    }

    let indices = &posting_list[&term];
    return indices[binary_search_prev(indices, 1, indices.len()-1, posting_index)];
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