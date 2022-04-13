package com.wararaki.sample_redis_messaging

import org.slf4j.Logger
import org.slf4j.LoggerFactory
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean
import org.springframework.data.redis.connection.RedisConnectionFactory
import org.springframework.data.redis.core.StringRedisTemplate
import org.springframework.data.redis.listener.RedisMessageListenerContainer
import org.springframework.data.redis.listener.adapter.MessageListenerAdapter
import org.springframework.data.redis.listener.PatternTopic

@SpringBootApplication
class SampleRedisMessagingApplication {
	companion object {
		val LOGGER: Logger = LoggerFactory.getLogger(this::class.java.enclosingClass)
	}

	@Bean
	fun container(connectionFactory: RedisConnectionFactory, listenerAdapter: MessageListenerAdapter): RedisMessageListenerContainer {
		val container = RedisMessageListenerContainer()
		container.setConnectionFactory(connectionFactory)
		container.addMessageListener(listenerAdapter, new PatternTopic("chat"))
		return container
	}

	@Bean
	fun listenerAdapter(receiver: Receiver): MessageListenerAdapter {
		val adapter = new MessageListenerAdapter(receiver, "receiveMessage")
	}

	@Bean
	fun receiver(): Receiver {
		return new Receiver()
	}

	@Bean
	fun template(connectionFactory: RedisConnectionFactory): StringRedisTemplate {
		return new StringRedisTemplate(connectionFactory)
	}
}

fun main(args: Array<String>) {
	runApplication<SampleRedisMessagingApplication>(*args)
	val template: StringRedisTemplate
}
