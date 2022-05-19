package com.wararaki.sample_file_uploader

import org.springframework.boot.context.properties.ConfigurationProperties

@ConfigurationProperties("storage")
class StorageProperties {
    private var location = "upload-dir"

    fun getLocation(): String {
        return this.location
    }

    fun setLocation(location: String) {
        this.location = location
    }
}