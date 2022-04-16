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
	@Bean
	fun container(connectionFactory: RedisConnectionFactory, listenerAdapter: MessageListenerAdapter): RedisMessageListenerContainer {
		val container = RedisMessageListenerContainer()
		val chat = PatternTopic("chat")
		container.setConnectionFactory(connectionFactory)
		container.addMessageListener(listenerAdapter, chat)

		return container
	}

	@Bean
	fun listenerAdapter(receiver: Receiver): MessageListenerAdapter {
		return MessageListenerAdapter(receiver, "receiveMessage")
	}

	@Bean
	fun receiver(): Receiver {
		return Receiver()
	}

	@Bean
	fun template(connectionFactory: RedisConnectionFactory): StringRedisTemplate {
		return StringRedisTemplate(connectionFactory)
	}
}

fun main(args: Array<String>) {
	val logger: Logger = LoggerFactory.getLogger("main")
	val context = runApplication<SampleRedisMessagingApplication>(*args)
	val template: StringRedisTemplate = context.getBean(StringRedisTemplate::class.java)
	val receiver: Receiver = context.getBean(Receiver::class.java)

	while (receiver.getCount() == 0) {
		logger.info("Sending message...")
		template.convertAndSend("chat", "hello from redis!")
		Thread.sleep(500L)
	}
}
