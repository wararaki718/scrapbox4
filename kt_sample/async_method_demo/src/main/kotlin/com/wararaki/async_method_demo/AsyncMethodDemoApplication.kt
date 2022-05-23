package com.wararaki.async_method_demo

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor

import java.util.concurrent.Executor


@SpringBootApplication
class AsyncMethodDemoApplication {
	@Bean
	fun taskExecuter(): Executor {
		val executor = ThreadPoolTaskExecutor()
		executor.corePoolSize = 2
		executor.maxPoolSize = 2
		executor.setQueueCapacity(500)
		executor.setThreadNamePrefix("GithubLookup-")
		executor.initialize()
		return executor
	}
}

fun main(args: Array<String>) {
	val context = runApplication<AsyncMethodDemoApplication>(*args)
	context.close()
}
