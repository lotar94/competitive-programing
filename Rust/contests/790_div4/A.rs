use std::io;

//https://rocket.rs/


fn main() {
    let mut tests = Int::new();

    io::stdin()
        .read_line(&mut tests)
        .expect("Failed to read line");

    println!("You guessed: {}", tests);

    println!("{:?}", tests.chars().enumerate());
    
    // const tickets: [i32; tests.chars().enumerate()] = [];

    // for (index, element) in tests.chars().enumerate() {
    //     println!("The value {} The index {}", element, index);
           
    // }
}
