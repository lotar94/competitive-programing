use std::io;

fn main() {
  let mut input_val: String = String::new();
  io::stdin()
      .read_line(&mut input_val)
      .expect("Failed to read line");
  // let input_val = input_val.trim();


  println!("{}",input_val);
  

  // println!("First Element {}", input_val.chars().next().unwrap());
  // println!("Last Element {}", input_val.chars().last().unwrap());
  // println!("The lenght of the string {}", input_val.len() - 1);
}