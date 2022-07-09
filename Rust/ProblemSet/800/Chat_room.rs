use std::io;

fn main() {
    let mut s = String::new();

    let xs = [ ^^^ ];
    //let xs: [i32] = [];

    io::stdin()
        .read_line(&mut s)
        .expect("Failed to read line");

    for (index, element) in s.chars().enumerate() {
        println!("The value {} The index {}", element, index);
        xs[index] = element
        println!("x =====> {:?}", xs[index]);
    }

}