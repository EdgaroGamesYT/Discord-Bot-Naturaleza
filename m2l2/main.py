import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$NaturalezaVideo'):
        await message.channel.send("https://youtu.be/USpBzWKhfoo ")
    if message.content.startswith('$ResumenNaturaleza'):
        await message.channel.send("La naturaleza es el entorno natural que nos rodea, incluyendo la flora, fauna, suelo, agua y el aire. Cuidarla es esencial para nuestra supervivencia y bienestar, ya que nos proporciona recursos y servicios vitales como el aire limpio, agua potable, alimentos y materias primas. Para protegerla, podemos adoptar hábitos sostenibles como reducir el consumo de recursos, reciclar, usar transporte público y apoyar prácticas comerciales responsables. ")
    elif message.content.startswith('$IdeasParaManualidades'):
        await message.channel.send("Para manualidades simples y cortas, puedes crear semilleros con vasos de plástico, muñecos de nieve con vasos de plástico, o un conejo decorativo con un plato de plástico. Otra opción es hacer un marco de fotos con palitos de paleta, un cohete con cajas o un avioneta con un rollo de papel higiénico. ")
    elif message.content.startswith('$TemaySignificado'):
        await message.channel.send('La naturaleza es crucial para la supervivencia de los seres vivos y para la salud del planeta. Nos proporciona un hogar, nos alimenta, nos limpia el agua y nos permite respirar aire limpio. La naturaleza también es fuente de inspiración y belleza, y nos brinda oportunidades para el descanso y la relajación. ')
    elif message.content.startswith('$EfectosContaminacion'):
        await message.channel.send('La contaminación de la naturaleza tiene graves efectos, incluyendo el deterioro de la calidad del aire y el agua, la pérdida de biodiversidad, el cambio climático y la degradación del suelo. Estos problemas pueden provocar daños a la salud humana, impactar en la economía, desplazar a las poblaciones y poner en peligro la supervivencia de especies.') 
    else:
        await message.channel.send(message.content)
client.run("TOKEN AQUI")




