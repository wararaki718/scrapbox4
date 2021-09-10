mod query;

use query::Query;


fn is_edge(query: Query) -> bool {
    return !((*query.right).is_some() && (*query.left).is_some());
}


fn main() {
    let q1 = Query::new(String::from("test"), None, None);
    println!("query1: {:?}", q1);
    println!("query1 is edge: {}", is_edge(q1));
    println!("");

    let qr = Query::new(String::from("right"), None, None);
    let ql = Query::new(String::from("left"), None, None);
    let q2 = Query::new(String::from("test2"), Some(qr), Some(ql));
    println!("query2: {:?}", q2);
    println!("query2 is edge: {}", is_edge(q2));

    println!("DONE");
}
