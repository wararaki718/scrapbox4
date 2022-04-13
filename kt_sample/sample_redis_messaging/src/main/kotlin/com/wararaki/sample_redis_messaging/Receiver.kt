package com.wararaki.sample_redis_messaging

import java.util.concurrent.atomic.AtomicInteger

import org.slf4j.Logger
import org.slf4j.LoggerFactory

class Receiver {
    companion object {
        val LOGGER: Logger = LoggerFactory.getLogger(this::class.java.enclosingClass)
        val counter: AtomicInteger = new AtomicInteger(0)
    }

    fun receiveMessage(message: String) {
        LOGGER.info("Received <%s>".format(message))
        counter.incrementAndGet()
    }

    fun getCount(): int {
        return counter.get()
    }
}