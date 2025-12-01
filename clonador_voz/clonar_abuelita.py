from coqui_tts.api import TTS

def clone_voice(text, speaker_wav, output_path):
    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/vits",
        progress_bar=True,
        gpu=False,           # pon gpu=True si tienes CUDA
    )
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language="es",
        file_path=output_path
    )

if __name__ == "__main__":
    speaker = "abuelita_22k.wav"
    texto = input("Texto a decir (en español): ")
    salida = "abuelita_output.wav"
    clone_voice(texto, speaker, salida)
    print(f"🔊 Audio generado en: {salida}")
