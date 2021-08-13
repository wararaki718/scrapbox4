mod next_phrase_with_binary_search;
mod posting_list;

use next_phrase_with_binary_search::next_phrase;
use posting_list::get_posting_list;


fn main() {
    let posting_list = get_posting_list();

    let terms = vec!["first".to_string(), "second".to_string()];
    let position = i32::MIN;
    let result = next_phrase(terms, position, &posting_list);
    println!("{:?}", result);
    println!("DONE");
}