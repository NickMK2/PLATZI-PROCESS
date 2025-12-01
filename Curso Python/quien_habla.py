from pyannote.audio.pipelines import SpeakerDiarization
from pyannote.core import Segment
import torch

pipeline = SpeakerDiarization.from_pretrained("pyannote/speaker-diarization")
pipeline.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

diarization = pipeline("ruta/del/audio.wav")

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start:.1f} - {turn.end:.1f}: {speaker}")
