package com.wararaki.sample_file_uploader

open class StorageException: RuntimeException {
    constructor(message: String, ex: Exception?): super(message, ex) {}
    constructor(message: String): super(message) {}
    constructor(ex: Exception): super(ex) {}
}
