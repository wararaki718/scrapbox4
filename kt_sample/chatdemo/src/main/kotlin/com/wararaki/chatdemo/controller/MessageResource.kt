package com.wararaki.chatdemo.controller

import com.wararaki.chatdemo.service.MessageService
import com.wararaki.chatdemo.service.MessageViewModel
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/v1/messages")
class MessageResource (val messageService: MessageService){
    @GetMapping
    suspend fun latest(@RequestParam(value="lastMessageId", defaultValue = "") lastMessageId: String): ResponseEntity<List<MessageViewModel>> {
        val messages = if (lastMessageId.isNotEmpty()) {
            messageService.after(lastMessageId)
        } else {
            messageService.latest()
        }

        return if (messages.isEmpty()) {
            with (ResponseEntity.noContent()) {
                header("lastMessageId", lastMessageId)
                build<List<MessageViewModel>>()
            }
        } else {
            with (ResponseEntity.ok()) {
                header("lastMessageId", messages.last().id)
                body(messages)
            }
        }
    }

    @PostMapping
    suspend fun post(@RequestBody message: MessageViewModel) {
        messageService.post(message)
    }
}