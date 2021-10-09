use std::collections::HashMap;

pub fn get_text() -> Vec<&'static str>{
    let docs = vec![
        "shakespeareanism"
    ];
    return docs;
}

pub fn get_dictionary() -> HashMap<String, Vec<String>> {
    let entry = vec![
        String::from("shakespeare"),
        String::from("shakespearean"),
        String::from("shakespeareanism"),
    ];
    let mut dictionary: HashMap<String, Vec<String>> = HashMap::new();
    dictionary.insert(String::from("shakespeareanism"), entry);

    return dictionary;
}
