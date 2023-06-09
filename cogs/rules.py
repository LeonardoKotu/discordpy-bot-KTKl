import disnake
from disnake.ext import commands
from main import bot

class Menu(disnake.ui.View):
	def __init__(self):
		super().__init__(timeout=None)

	@disnake.ui.select(
		placeholder="Нажмите для выбора",
		custom_id="menu1",
		options = 
		[
			disnake.SelectOption(
				label="Общие правила",
				emoji="<:blue_white_dot:1101996010634481666>"
			),
			disnake.SelectOption(
				label="Голосовые",
				emoji="<:blue_white_dot:1101996010634481666>"
			),
			disnake.SelectOption(
				label="Виды нарушений",
				emoji="<:blue_white_dot:1101996010634481666>"
			),
			disnake.SelectOption(
				label="Снять выбор",
				emoji="<:blue_white_dot:1101996010634481666>"
			)
		]
	)
#FF1660
	async def select_callback(self, select, interaction):
		if select.values[0] == "Общие правила":
			# Эмбеды общих положение
			# 1.0
			embed = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`1.0`**",
				colour=0x2f3136
			)

			embed.add_field(
				name="> Описание",
				value="```Обход бана и других нарушений / использование запасных аккаунтов```",
				inline=False
			)

			embed.add_field(
				name="> Нарушение",
				value=
				"```Мьют/бан```",
				inline=True
			)

			embed.add_field(
				name="> Длительность",
				value="```20ч/30д```",
				inline=True
			)

			# 1.1
			embed2 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`1.1`**",
				colour=0x2f3136
			)

			embed2.add_field(
				name="> Описание",
				value="```Коммерческая реклама и пиар без соглашении Администраций.```",
				inline=False
			)

			embed2.add_field(
				name="> Нарушение",
				value=
				"```Бан```",
				inline=True
			)

			embed2.add_field(
				name="> Длительность",
				value="```Навсегда```",
				inline=True
			)

			# 1.1
			embed3 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`1.2`**",
				colour=0x2f3136
			)

			embed3.add_field(
				name="> Описание",
				value="```Коммерческая реклама и пиар без соглашении Администраций.```",
				inline=False
			)

			embed3.add_field(
				name="> Нарушение",
				value=
				"```Бан```",
				inline=True
			)


			# 1.2
			embed4 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`1.3`**",
				colour=0x2f3136
			)

			embed4.add_field(
				name="> Описание",
				value="```Запрещена публикация шокирующего и сексуального контента.```",
				inline=False
			)

			embed4.add_field(
				name="> Нарушение",
				value=
				"```Варн/мьют```",
				inline=True
			)

			embed4.add_field(
				name="> Длительность",
				value="```6д/2ч```",
				inline=True
			)



			# 1.3
			embed5 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`1.4`**",
				colour=0x2f3136
			)

			embed5.add_field(
				name="> Описание",
				value="```Запрещена публикация шокирующего и сексуального контента.```",
				inline=False
			)

			embed5.add_field(
				name="> Нарушение",
				value=
				"```Варн/мьют```",
				inline=True
			)

			embed5.add_field(
				name="> Длительность",
				value="```6д/2ч```",
				inline=True
			
			)


			# 1.4
			embed6 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`1.5`**",
				colour=0x2f3136
			)

			embed6.add_field(
				name="> Описание",
				value="```Запрещено массовое упоминание пользователей и ролей.```",
				inline=False
			)

			embed6.add_field(
				name="> Нарушение",
				value=
				"```Варн/мьют```",
				inline=True
			)

			embed6.add_field(
				name="> Длительность",
				value="```6д/2ч```",
				inline=True
			)


			embed.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed2.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed3.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed4.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed5.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed6.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")


			await interaction.send(embeds=[embed, embed2, embed3, embed4, embed5, embed6], ephemeral=True)

		if select.values[0] == "Голосовые":

			# 2.0 - Голсоовые
			embed7 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`2.0`**",
				colour=0x2f3136
			)

			embed7.add_field(
				name="> Описание",
				value="""```Нельзя включать музыку в микрофон.```""",
				inline=False
			)

			embed7.add_field(
				name="> Нарушение",
				value="""```Варн/мьют```""",
				inline=True
			)

			embed7.add_field(
				name="> Длительность",
				value="""```5д/2ч```""",
				inline=True
			)


			# 2.1 - Голсоовые
			embed8 = disnake.Embed(
				title="<:white_dot2:1101889261432737844> Пункт - **`2.1`**",
				colour=0x2f3136
			)


			embed8.add_field(
				name="> Нарушение",
				value="""```Варн/мьют```""",
				inline=True
			)

			embed8.add_field(
				name="> Описание",
				value="""```Не допускается издание громких звуков в микрофон.```""",
				inline=False
			)


			embed8.add_field(
				name="> Длительность",
				value="""```5д/2ч```""",
				inline=True
			)


			# 2.2 - Голсоовые
			embed9 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`2.2`**",
				colour=0x2f3136
			)

			embed9.add_field(
				name="> Описание",
				value="""```При наличии шума вокруг рекомендуется применение Push-To-Talk..```""",
				inline=False
			)



			embed9.add_field(
				name="> Нарушение",
				value="""```Варн/мьют```""",
				inline=True
			)


			embed9.add_field(
				name="> Длительность",
				value="""```5д/2ч```""",
				inline=True
			)


			# 2.3 - Голсоовые
			embed10 = disnake.Embed(
				title="<:blue_white_dot:1101996010634481666> Пункт - **`2.3`**",
				colour=0x2f3136
			)

			embed10.add_field(
				name="> Описание",
				value="""```При наличии шума вокруг рекомендуется применение Push-To-Talk..```""",
				inline=False
			)


			embed10.add_field(
				name="> Нарушение",
				value="""```Варн/мьют```""",
				inline=True
			)


			embed10.add_field(
				name="> Длительность",
				value="""```5д/2ч```""",
				inline=True
			)

			embed7.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed8.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed9.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")
			embed10.set_image(url="https://cdn.discordapp.com/attachments/1100945663283437578/1104174486284152883/image.png")


			await interaction.send(embeds=[embed7, embed8, embed9, embed10], ephemeral=True)

		if select.values[0] == "Виды нарушений":
			embed_n = disnake.Embed(
				title="Виды наказаний на сервере Amnesia",
				description=
				"""
				> <:blue_white_dot:1101996010634481666> **Варн** - предупреждение для участника.
				> <:blue_white_dot:1101996010634481666> **Мьют** - временная блокировка сервера.
				> <:blue_white_dot:1101996010634481666> **Бан** - полная блокировка участника.

				""",
				colour=0xe81a51
			)

			await interaction.response.send_message(embed=embed_n, ephemeral=True)



		if select.values[0] == "Снять выбор":
			await interaction.response.send_message("^^Успешно", ephemeral=True)

class Rules(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		bot.add_view(view=Menu())


	@commands.slash_command()
	async def rules1(self, inter):
		pass	

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content == "$serverrules":
			img = disnake.Embed(colour=0x2f3136)
			img.set_image(url='https://i.pinimg.com/originals/f1/18/30/f118307225c557ea9c083486da5c1c42.gif')

			embed = disnake.Embed(

				title = "<:blue_white_dot:1101996010634481666> Правила сервера Amnesia",
				description=
				"""
				> `::` Мы рекомендуем прочитать *правила*, чтобы сервер был **чистым** и **спокойным**.
				> Так же наш сервер, придерживается к 
				> - **[Discord ToS](https://discord.com/terms)** *и* **[Discord Guildlines](https://discord.com/guidelines)**
				""",
				colour=0x2f3136
			)

			embed.set_image(url="https://i.pinimg.com/564x/88/e3/94/88e3941bd4f4b25313f6fbe375114605.jpg")

			await message.channel.send(embeds=[img, embed], view=Menu())


def setup(bot):
	bot.add_cog(Rules(bot))
