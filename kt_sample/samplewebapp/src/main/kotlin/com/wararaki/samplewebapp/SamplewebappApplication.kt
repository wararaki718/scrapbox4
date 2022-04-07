package com.wararaki.samplewebapp

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class SamplewebappApplication

fun main(args: Array<String>) {
	runApplication<SamplewebappApplication>(*args)
}
