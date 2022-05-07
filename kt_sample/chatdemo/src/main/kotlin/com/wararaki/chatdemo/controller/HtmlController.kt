package com.wararaki.chatdemo.controller

import com.wararaki.chatdemo.service.MessageService
import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.GetMapping

@Controller
class HtmlController (val messageService: MessageService) {
    @GetMapping("/")
    suspend fun index(model: Model): String {
        return "chatrs"
    }
}