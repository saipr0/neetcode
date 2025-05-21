#[allow(dead_code)]
pub fn contains_duplicate(nums: Vec<i32>) -> bool {
    use std::collections::HashSet;
    let mut seen = HashSet::new();
    for num in nums {
        if !seen.insert(num) {
            return true;
        }
    }
    false
}

#[cfg(test)] // Only compile this block when running cargo test
mod tests {
    use super::*; // Bring `contains_duplicate` into scope

    #[test] // Marks this as a test
    fn no_duplicates() {
        assert_eq!(contains_duplicate(vec![1, 2, 3]), false);
        assert_eq!(contains_duplicate(vec![1]), false);
    }

    #[test] // Marks this as a test
    fn duplicates() {
        assert_eq!(contains_duplicate(vec![1, 1]), true);
        assert_eq!(contains_duplicate(vec![1, 2, 3, 1]), true);
    }
}
