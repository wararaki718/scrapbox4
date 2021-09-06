use std::collections::HashMap;

use crate::posting::Posting;


static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;


pub fn docid(position: Posting) -> i32 {
    return position.docid;
}


pub fn offset(position: Posting) -> i32 {
    return position.offset;
}


pub fn first(term: String, posting_list: &HashMap<String, Vec<Posting>>) -> Posting {
    if posting_list.contains_key(&term) {
        if let Some(posting) = posting_list[&term].first() {
            return *posting;
        }
    }
    return Posting::new(NEG_INF, NEG_INF);
}


pub fn last(term: String, posting_list: &HashMap<String, Vec<Posting>>) -> Posting {
    if posting_list.contains_key(&term) {
        if let Some(posting) = posting_list[&term].last() {
            return *posting;
        }
    }
    return Posting::new(INF, INF);
}


pub fn next(term: String, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> Posting {
    if docid(current) == INF || offset(current) == INF {
        return Posting::new(INF, INF);
    }
    
    if docid(current) == NEG_INF || offset(current) == NEG_INF {
        return first(term, &posting_list);
    }

    let postings = &posting_list[&term];
    for posting in postings {
        if docid(current) <= docid(*posting) && offset(current) < offset(*posting) {
            return *posting;
        }
    }

    return Posting::new(INF, INF);
}


pub fn prev(term: String, current: Posting, posting_list: &HashMap<String, Vec<Posting>>) -> Posting {
    if docid(current) == NEG_INF || offset(current) == NEG_INF {
        return Posting::new(NEG_INF, NEG_INF);
    }

    if docid(current) == INF || offset(current) == INF {
        return last(term, &posting_list);
    }

    let postings = &posting_list[&term];
    for posting in postings {
        if docid(current) >= docid(*posting) && offset(current) > offset(*posting) {
            return *posting;
        }
    }

    return Posting::new(NEG_INF, NEG_INF);
}
