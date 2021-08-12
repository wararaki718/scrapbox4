use std::collections::HashMap;

static INF: i32 = i32::MAX;
static NEG_INF: i32 = i32::MIN;

pub fn get_posting_list() -> HashMap<String, Vec<i32>> {
    let v = vec![NEG_INF, 11, 22, 33, 66, INF];
    let v2 = vec![NEG_INF, 8, 9, 12, INF];
    let v3 = vec![NEG_INF, 77, 88, 99, INF];
    let mut posting_list = HashMap::new();
    posting_list.insert("first".to_string(), v);
    posting_list.insert("second".to_string(), v2);
    posting_list.insert("third".to_string(), v3);

    return posting_list;
}
