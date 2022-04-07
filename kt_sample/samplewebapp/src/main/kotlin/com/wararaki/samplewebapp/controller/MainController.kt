package com.wararaki.samplewebapp.controller

import com.wararaki.samplewebapp.model.User
import com.wararaki.samplewebapp.repo.UserRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*

@Controller
@RequestMapping("/demo")
class MainController {
    @Autowired
    lateinit var repository: UserRepository

    @PostMapping("/add")
    @ResponseBody
    fun addNewUser(@RequestParam name: String, @RequestParam email: String): String {
        repository.save(User(name, email))
        return "Saved"
    }

    @GetMapping("/all")
    @ResponseBody
    fun getAllUsers() = repository.findAll()
}