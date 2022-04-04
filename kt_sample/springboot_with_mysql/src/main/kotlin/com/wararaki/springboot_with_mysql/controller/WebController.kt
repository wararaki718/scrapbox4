package com.wararaki.springboot_with_mysql.controller

import com.wararaki.springboot_with_mysql.model.Customer
import com.wararaki.springboot_with_mysql.repo.CustomerRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController


@RestController
class WebController {
    @Autowired
    lateinit var repository: CustomerRepository

    @RequestMapping("/save")
    fun save(): String {
        repository.save(Customer("Jack", "Smith"))
        repository.save(Customer("Adam", "Johnson"))
        repository.save(Customer("Test", "User"))
        repository.save(Customer("Example", "Sample"))
        repository.save(Customer("ABC", "XYZ"))

        return "Done"
    }

    @RequestMapping("/findall")
    fun findAll() = repository.findAll()

    @RequestMapping("/findbyid/{id}")
    fun findById(@PathVariable id: Long) = repository.findById(id)

    @RequestMapping("/findbylastname/{lastName}")
    fun findByLastName(@PathVariable lastName: String) = repository.findByLastName(lastName)
}
