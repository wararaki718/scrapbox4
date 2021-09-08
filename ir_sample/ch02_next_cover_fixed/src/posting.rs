use std::cmp::Ordering;

#[derive(Clone, Copy, Debug, Eq)]
pub struct Posting {
    pub docid: i32,
    pub offset: i32,
}

impl Posting {
    pub fn new(docid: i32, offset: i32) -> Self {
        Self {
            docid,
            offset
        }
    }
}

impl Ord for Posting {
    fn cmp(&self, other: &Self) -> Ordering {
        if self.docid < other.docid {
            return Ordering::Less;
        } else if self.docid == other.docid && self.offset == other.offset {
            return Ordering::Equal;
        } else if self.docid == other.docid && self.offset < other.offset {
            return Ordering::Less;
        } else {
            return Ordering::Greater;
        }
    }
}

impl PartialOrd for Posting {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Posting {
    fn eq(&self, other: &Self) -> bool {
        self.docid == other.docid && self.offset == other.offset
    }
}