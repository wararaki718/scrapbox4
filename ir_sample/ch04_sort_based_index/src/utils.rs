use std::collections::HashMap;

pub fn get_text() -> Vec<&'static str>{
    let docs = vec![
        "<SPEECH> <SPEAKER> GREGORY </SPEAKER> <LINE> Do you quarrel, sir? </LINE> </SPEECH>",
        "<SPEECH> <SPEAKER> ABRAHAM </SPEAKER> <LINE> Quarrel sir! no, sir.</LINE> </SPEECH>"
    ];
    return docs;
}

pub fn get_dictionary(texts: Vec<String>) -> HashMap<String, usize> {
    let mut dictionary: HashMap<String, usize> = HashMap::new();
    let mut uid: usize = 1;
    for text in texts {
        for term in text.split(" ") {
            if !dictionary.contains_key(term) {
                dictionary.insert((&term).to_string(), uid);
                uid += 1;
            }
        }
    }

    return dictionary;
}
