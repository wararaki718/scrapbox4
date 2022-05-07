package com.wararaki.chatdemo

import app.cash.turbine.test
import com.wararaki.chatdemo.repository.MessageRepository
import org.junit.jupiter.api.BeforeEach
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import java.time.Instant
import com.wararaki.chatdemo.Model.ContentType
import com.wararaki.chatdemo.Model.Message
import com.wararaki.chatdemo.service.MessageViewModel
import com.wararaki.chatdemo.service.UserViewModel
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Test
import org.springframework.boot.web.server.LocalServerPort
import org.springframework.messaging.rsocket.RSocketRequester
import org.springframework.messaging.rsocket.dataWithType
import org.springframework.messaging.rsocket.retrieveFlow
import java.net.URI
import java.net.URL
import java.time.temporal.ChronoUnit.MILLIS
import kotlin.time.Duration.Companion.seconds
import kotlin.time.ExperimentalTime
import kotlinx.coroutines.flow.collect

@SpringBootTest(
	webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT,
	properties = [
		"spring.r2dbc.url=r2dbc:h2:mem:///testdb;USER=sa;PASSWORD=password"
	]
)
class ChatdemoApplicationTests(
	@Autowired val rsocketBuilder: RSocketRequester.Builder,
	@Autowired val messageRepository: MessageRepository,
	@LocalServerPort val serverPort: Int
) {
	lateinit var lastMessageId: String

	val now: Instant = Instant.now()

	@BeforeEach
	fun setUp() {
		runBlocking {
			val secondBeforeNow = now.minusSeconds(1)
			val twoSecondBeforeNow = now.minusSeconds(2)
			val savedMessages = messageRepository.saveAll(
				listOf(
					Message(
						"*testMessage*",
						ContentType.PLAIN,
						twoSecondBeforeNow,
						"test",
						"http://test.com"
					),
					Message(
						"**testMessage2**",
						ContentType.MARKDOWN,
						secondBeforeNow,
						"test1",
						"http://test.com"
					),
					Message(
						"`testMessage3`",
						ContentType.MARKDOWN,
						now,
						"test2",
						"http://test.com"
					)
				)
			)
			lastMessageId = savedMessages.first().id ?: ""
		}
	}

	@AfterEach
	fun tearDown() {
		runBlocking {
			messageRepository.deleteAll()
		}
	}

	@ExperimentalTime
	@ExperimentalCoroutinesApi
	@Test
	fun `test that messages API streams latest messages`() {
		runBlocking {
			val rSocketRequester =
				rsocketBuilder.websocket(URI("ws://localhost:${serverPort}/rsocket"))

			rSocketRequester
				.route("api.v1.messages.stream")
				.retrieveFlow<MessageViewModel>()
				.test {
					assertThat(expectItem().prepareForTesting())
						.isEqualTo(
							MessageViewModel(
								"*testMessage*",
								UserViewModel("test", URL("http://test.com")),
								now.minusSeconds(2).truncatedTo(MILLIS)
							)
						)

					assertThat(expectItem().prepareForTesting())
						.isEqualTo(
							MessageViewModel(
								"<body><p><strong>testMessage2</strong></p></body>",
								UserViewModel("test1", URL("http://test.com")),
								now.minusSeconds(1).truncatedTo(MILLIS)
							)
						)
					assertThat(expectItem().prepareForTesting())
						.isEqualTo(
							MessageViewModel(
								"<body><p><code>testMessage3</code></p></body>",
								UserViewModel("test2", URL("http://test.com")),
								now.truncatedTo(MILLIS)
							)
						)

					expectNoEvents()

					launch {
						rSocketRequester.route("api.v1.messages.stream")
							.dataWithType(flow {
								emit(
									MessageViewModel(
										"`HelloWorld`",
										UserViewModel("test", URL("http://test.com")),
										now.plusSeconds(1)
									)
								)
							})
							.retrieveFlow<Void>()
							.collect()
					}

					assertThat(expectItem().prepareForTesting())
						.isEqualTo(
							MessageViewModel(
								"<body><p><code>HelloWorld</code></p></body>",
								UserViewModel("test", URL("http://test.com")),
								now.plusSeconds(1).truncatedTo(MILLIS)
							)
						)

					cancelAndIgnoreRemainingEvents()
				}
		}
	}

	@ExperimentalTime
	@Test
	fun `test that messages streamed to the API is stored`() {
		runBlocking {
			launch {
				val rSocketRequester =
					rsocketBuilder.websocket(URI("ws://localhost:${serverPort}/rsocket"))

				rSocketRequester.route("api.v1.messages.stream")
					.dataWithType(flow {
						emit(
							MessageViewModel(
								"`HelloWorld`",
								UserViewModel("test", URL("http://test.com")),
								now.plusSeconds(1)
							)
						)
					})
					.retrieveFlow<Void>()
					.collect()
			}

			delay(2.seconds)

			messageRepository.findAll()
				.first { it.content.contains("HelloWorld") }
				.apply {
					assertThat(this.prepareForTesting())
						.isEqualTo(
							Message(
								"`HelloWorld`",
								ContentType.MARKDOWN,
								now.plusSeconds(1).truncatedTo(MILLIS),
								"test",
								"http://test.com"
							)
						)
				}
		}
	}
}

