package com.wararaki.chatdemo.controller

import com.wararaki.chatdemo.service.MessageService
import com.wararaki.chatdemo.service.MessageViewModel
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.emitAll
import kotlinx.coroutines.flow.onStart
import org.springframework.messaging.handler.annotation.MessageMapping
import org.springframework.messaging.handler.annotation.Payload
import org.springframework.stereotype.Controller

@Controller
@MessageMapping("api.v1.messages")
class MessageResource (val messageService: MessageService){
    @MessageMapping("stream")
    suspend fun receive(@Payload inboundMessages: Flow<MessageViewModel>) =
        messageService.post(inboundMessages)

    @MessageMapping("stream")
    fun send(): Flow<MessageViewModel> = messageService
        .stream()
        .onStart {
            emitAll(messageService.latest())
        }
}