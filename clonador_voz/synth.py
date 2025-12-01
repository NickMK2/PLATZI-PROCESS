from TTS.api import TTS

# 1. Carga el modelo VITS multilingüe
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/vits",
    progress_bar=True,
    gpu=False  # o True si tienes GPU NVidia+Cuda
)

# 2. Tu texto
texto = """A mi querida familia,

Los amé antes y los amo ahora. No se aflijan por mi partida. Estoy siguiendo el camino que Dios dispuso y tomé su mano cuando Él decidió llamarme; encontré esa paz al final del día. Les agradezco a todos por cada momento feliz que compartimos y por ese gran cariño que me brindan. Gracias por esos hermosos momentos en familia, de amor, sinceridad y regocijo.

Pero ha llegado el tiempo de partir. Solo lloren por mí un instante si se sienten afligidos. Después, dejen que su pesar sea reemplazado por la confianza de que un día cada vez más cercano nos uniremos nuevamente, pues yo solo me estoy adelantando en el camino que todos recorrerán.

Les pido que me recuerden con alegría y se mantengan en paz y unidos. Igualmente, yo no estaré lejos y la vida continúa. Mientras yo viva en sus corazones, en su memoria, no me iré para siempre. Y después, cuando ustedes tengan que viajar solos por este camino, yo los recibiré con una sonrisa y les diré: "Bienvenidos a casa".

A mi querida y hermosa familia, que la vida de ustedes siga siendo bella y hermosa y que Dios los acompañe siempre por donde vayan.

Amén."""

# 3. Genera el audio clonando la voz de tu abuelita
#    asegúrate de haber convertido su WAV a 22 kHz (abuelita_22k.wav)
tts.tts_with_vc_to_file(
    text=texto,
    speaker_wav="abuelita_22k.wav",
    language="es",
    file_path="abuelita_clonada.wav"
)

print("¡Listo! Audio generado en abuelita_clonada.wav")
