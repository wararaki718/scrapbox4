package com.wararaki.chatdemo.service

import com.wararaki.chatdemo.asDomainObject
import com.wararaki.chatdemo.mapToViewModel
import com.wararaki.chatdemo.repository.MessageRepository
import org.springframework.context.annotation.Primary
import org.springframework.stereotype.Service

@Service
@Primary
class PersistentMessageService(val messageRepository: MessageRepository) : MessageService {
    override fun latest(): List<MessageViewModel> = messageRepository.findLatest().mapToViewModel()

    override fun after(lastMessageId: String): List<MessageViewModel> = messageRepository.findLatest(lastMessageId).mapToViewModel()

    override fun post(message: MessageViewModel) {
        messageRepository.save(message.asDomainObject())
    }
}