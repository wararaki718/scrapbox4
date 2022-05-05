package com.wararaki.chatdemo

import com.wararaki.chatdemo.Model.ContentType
import com.wararaki.chatdemo.Model.Message
import com.wararaki.chatdemo.service.MessageViewModel
import com.wararaki.chatdemo.service.UserViewModel
import org.intellij.markdown.flavours.commonmark.CommonMarkFlavourDescriptor
import org.intellij.markdown.html.HtmlGenerator
import org.intellij.markdown.parser.MarkdownParser
import java.net.URL

fun MessageViewModel.asDomainObject(contentType: ContentType = ContentType.MARKDOWN): Message = Message(
    content,
    contentType,
    sent,
    user.name,
    user.avatarImageLink.toString(),
    id
)

fun Message.asViewModel(): MessageViewModel = MessageViewModel(
    contentType.render(content),
    UserViewModel(username, URL(userAvatarImageLink)),
    sent,
    id
)

fun List<Message>.mapToViewModel(): List<MessageViewModel> = map { it.asViewModel() }

fun ContentType.render(content: String): String = when(this) {
    ContentType.PLAIN -> content
    ContentType.MARKDOWN -> {
        val flavour = CommonMarkFlavourDescriptor()
        HtmlGenerator(
            content,
            MarkdownParser(flavour).buildMarkdownTreeFromString(content),
            flavour
        ).generateHtml()
    }
}
