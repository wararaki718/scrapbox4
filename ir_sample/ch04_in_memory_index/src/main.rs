mod build_index;
mod normalize;
mod utils;

use build_index::build_index;
use normalize::normalize;
use utils::{get_text, get_dictionary};

fn main() {
    let texts = get_text();
    let dictionary = get_dictionary();
    
    let mut norm_texts = Vec::new();
    for text in texts {
        norm_texts.push(normalize(String::from(text)));
    }
    build_index(norm_texts, dictionary);
    
    println!("DONE");
}
