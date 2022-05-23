package com.wararaki.async_method_demo

import org.slf4j.LoggerFactory
import org.springframework.boot.CommandLineRunner
import org.springframework.stereotype.Component
import java.util.concurrent.CompletableFuture

@Component
class AppRunner(val githubLookupService: GithubLookupService ): CommandLineRunner {
    private final val logger = LoggerFactory.getLogger(AppRunner::class.java)

    override fun run(vararg args: String?) {
        val start = System.currentTimeMillis()

        val page1 = githubLookupService.findUser("PivotalSoftware")
        val page2 = githubLookupService.findUser("CloudFoundry")
        val page3 = githubLookupService.findUser("Spring-Projects")

        CompletableFuture.allOf(page1, page2, page3).join()

        val elapsedTime = (System.currentTimeMillis() - start)
        logger.info("Elapsed time: %d".format(elapsedTime))
        logger.info("--> %s".format(page1.get()))
        logger.info("--> %s".format(page2.get()))
        logger.info("--> %s".format(page3.get()))
    }
}