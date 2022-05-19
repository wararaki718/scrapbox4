package com.wararaki.sample_file_uploader

import org.springframework.boot.CommandLineRunner
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.context.properties.EnableConfigurationProperties
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean

@SpringBootApplication
@EnableConfigurationProperties(StorageProperties::class)
class SampleFileUploaderApplication {
	@Bean
	fun init(storageService: StorageService) = CommandLineRunner {
		storageService.deleteAll()
		storageService.init()
	}
}

fun main(args: Array<String>) {
	runApplication<SampleFileUploaderApplication>(*args)
}
