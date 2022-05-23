package com.wararaki.async_method_demo

import org.slf4j.LoggerFactory
import org.springframework.boot.web.client.RestTemplateBuilder
import org.springframework.scheduling.annotation.Async
import org.springframework.stereotype.Service
import java.util.concurrent.CompletableFuture

@Service
class GithubLookupService (val restTemplateBuilder: RestTemplateBuilder) {
    private final val logger = LoggerFactory.getLogger(GithubLookupService::class.java)
    private final val restTemplate = restTemplateBuilder.build()

    @Async
    fun findUser(user: String): CompletableFuture<User> {
        logger.info("Looking up %s".format(user))
        val url = "https://api.github.com/users/%s".format(user)
        val results = restTemplate.getForObject(url, User::class.java)

        Thread.sleep(1000L)
        return CompletableFuture.completedFuture(results)
    }
}