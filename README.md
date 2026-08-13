<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="A speech waveform resolving into discrete tokens" width="100%">
</picture>

### Ömer Yentür

I build speech systems: text-to-speech, speech recognition, and the training and
serving pipelines around them. Most of my work is on Turkish, where the pretrained
models are weaker and the interesting problems are in the data rather than the
architecture. I spend a lot of time on the unglamorous half of that, telephone-channel
robustness, alignment quality, tokenizer behaviour, and getting inference fast enough
to be worth deploying.

---

### Working with

Speech and audio — VoxCPM, Spark-TTS, Whisper and Qwen3-ASR fine-tuning, VAD,
diarization, forced alignment, codec and channel simulation.

Training — PyTorch, LoRA and full fine-tunes, multi-GPU (FSDP, DDP), MLX on Apple
silicon.

Serving — vLLM, CTranslate2, ONNX Runtime, sherpa-onnx, batched custom runtimes.

---

mr.yentur@gmail.com
