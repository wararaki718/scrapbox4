package com.wararaki.crudweb.spring_boot_with_postgresql

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class SpringBootWithPostgresqlApplication

fun main(args: Array<String>) {
	runApplication<SpringBootWithPostgresqlApplication>(*args)
}
