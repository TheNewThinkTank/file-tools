
import whisper

model = whisper.load_model("small")

infile = "~/Desktop/devops-in-pharma.wav"
outfile = infile.removesuffix("wav") + "txt"

result = model.transcribe(infile)

with open(outfile, "w") as wf:
    wf.write(result["text"])
