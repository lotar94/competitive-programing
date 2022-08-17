use std::io;

fn main() {
    let mut weight_watermelon: String = String::new();

    io::stdin()
        .read_line(&mut weight_watermelon)
        .expect("Failed to read line");

    let val:i32 =  weight_watermelon.trim().parse::<i32>().expect("error") ;

    if val%2 == 0 && val > 2{
        print!("YES")
    } else {
        print!("NO")
    }

}
