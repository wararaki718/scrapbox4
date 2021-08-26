use sample_divide_files::sample::Sample;


pub fn create_sample(name: String) -> Sample {
    println!("call create_sample function.");
    return Sample::new(name);
}
