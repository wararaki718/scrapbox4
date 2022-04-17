package com.wararaki.sample_webflux_application

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.ConfigurableApplicationContext

@SpringBootApplication
class SampleWebFluxApplication

fun main(args: Array<String>) {
	val context: ConfigurableApplicationContext = runApplication<SampleWebFluxApplication>(*args)

	val greetingClient: GreetingClient = context.getBean(GreetingClient::class.java)

	println(">> message = %s".format(greetingClient.getMessage().block()))
}
