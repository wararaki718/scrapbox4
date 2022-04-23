package com.wararaki.sample_react_springdata_web

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.CommandLineRunner
import org.springframework.stereotype.Component

@Component
class DatabaseLoader: CommandLineRunner {
    private var repository: EmployeeRepository

    @Autowired
    constructor(repository: EmployeeRepository) {
        this.repository = repository
    }

    override fun run(vararg args: String?) {
        this.repository.save(Employee("Frodo", "Baggins", "ring bearer"))
    }
}