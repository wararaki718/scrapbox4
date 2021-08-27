pub fn normalize(text: String) -> String {
    let mut tmp = text.to_lowercase();

    let symbols = ["!", "?", ",", "."];
    for symbol in symbols {
        tmp = tmp.replace(symbol, "");
    }

    return tmp;
}
