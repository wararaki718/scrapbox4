package com.wararaki.chatdemo

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class ChatdemoApplication

fun main(args: Array<String>) {
	runApplication<ChatdemoApplication>(*args)
}
