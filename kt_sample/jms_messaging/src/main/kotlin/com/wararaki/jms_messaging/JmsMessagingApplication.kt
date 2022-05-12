package com.wararaki.jms_messaging

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.autoconfigure.jms.DefaultJmsListenerContainerFactoryConfigurer
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean
import org.springframework.jms.annotation.EnableJms
import org.springframework.jms.config.DefaultJmsListenerContainerFactory
import org.springframework.jms.config.JmsListenerContainerFactory
import org.springframework.jms.core.JmsTemplate
import org.springframework.jms.support.converter.MappingJackson2MessageConverter
import org.springframework.jms.support.converter.MessageConverter
import org.springframework.jms.support.converter.MessageType
import javax.jms.ConnectionFactory

@SpringBootApplication
@EnableJms
class JmsMessagingApplication {
	@Bean
	fun myFactory(connectionFactory: ConnectionFactory, configurer: DefaultJmsListenerContainerFactoryConfigurer): DefaultJmsListenerContainerFactory {
		val factory = DefaultJmsListenerContainerFactory()
		configurer.configure(factory, connectionFactory)
		return factory
	}

	@Bean
	fun jacksonJmsMessageConverter(): MessageConverter {
		val converter = MappingJackson2MessageConverter()
		converter.setTargetType(MessageType.TEXT)
		converter.setTypeIdPropertyName("_type")
		return converter
	}
}

fun main(args: Array<String>) {
	val context = runApplication<JmsMessagingApplication>(*args)

	val jmsTemplate = context.getBean(JmsTemplate::class.java)

	println("Sending an email message")
	jmsTemplate.convertAndSend("mailbox", Email("info@example.com", "Hello"))
}
