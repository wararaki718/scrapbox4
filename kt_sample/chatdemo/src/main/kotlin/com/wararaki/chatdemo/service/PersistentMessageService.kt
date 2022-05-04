package com.wararaki.chatdemo.service

import com.wararaki.chatdemo.Model.ContentType
import com.wararaki.chatdemo.Model.Message
import com.wararaki.chatdemo.repository.MessageRepository
import org.springframework.context.annotation.Primary
import org.springframework.stereotype.Service
import java.net.URL

@Service
@Primary
class PersistentMessageService(val messageRepository: MessageRepository) : MessageService {
    override fun latest(): List<MessageViewModel> = messageRepository.findLatest().map{
        with (it) {
            MessageViewModel(content, UserViewModel(username, URL(userAvatarImageLink)), sent, id)
        }
    }

    override fun after(lastMessageId: String): List<MessageViewModel> = messageRepository.findLatest(lastMessageId).map {
        with (it) {
            MessageViewModel(content, UserViewModel(username, URL(userAvatarImageLink)), sent, id)
        }
    }

    override fun post(message: MessageViewModel) {
        messageRepository.save(
            with (message) {
                Message(content, ContentType.PLAIN, sent, user.name, user.avatarImageLink.toString())
            }
        )
    }
}