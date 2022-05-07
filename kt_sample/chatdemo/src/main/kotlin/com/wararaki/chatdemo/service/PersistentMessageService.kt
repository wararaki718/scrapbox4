package com.wararaki.chatdemo.service

import com.wararaki.chatdemo.asDomainObject
import com.wararaki.chatdemo.asRendered
import com.wararaki.chatdemo.mapToViewModel
import com.wararaki.chatdemo.repository.MessageRepository
import kotlinx.coroutines.flow.*
import org.springframework.stereotype.Service

@Service
class PersistentMessageService(val messageRepository: MessageRepository) : MessageService {
    val sender: MutableSharedFlow<MessageViewModel> = MutableSharedFlow()

    override fun latest(): Flow<MessageViewModel> = messageRepository.findLatest().mapToViewModel()

    override fun after(lastMessageId: String): Flow<MessageViewModel> = messageRepository.findLatest(lastMessageId).mapToViewModel()

    override fun stream(): Flow<MessageViewModel> = sender

    override suspend fun post(messages: Flow<MessageViewModel>) =
        messages
            .onEach { sender.emit(it.asRendered()) }
            .map {  it.asDomainObject() }
            .let { messageRepository.saveAll(it) }
            .collect()
}