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

### Selected work

| | |
|---|---|
| **[supertonic-v3-pytorch](https://github.com/yentur/supertonic-v3-pytorch)** | Supertonic-3 TTS reimplemented in pure PyTorch, reconstructed bit-exactly from the ONNX graph, plus a Turkish fine-tune. Written because the released weights had no training-capable implementation. |
| **[phone-augment](https://github.com/yentur/phone-augment)** | Telephone-channel augmentation for noise-robust ASR: RIR, additive noise, codec simulation and packet loss. Built after measuring which of those actually moves WER, and which makes it worse. |
| **[LLM-KAYNAK](https://github.com/yentur/LLM-KAYNAK)** | A curated map of LLM resources in Turkish. |
| **[HizliNot](https://github.com/yentur/HizliNot)** | Native macOS quick-note widget in Swift. Global hotkey, floating glass UI, a file shelf. Unrelated to the rest, built because I wanted it. |

---

### Upstream contributions

Recent patches to projects I use. Each one started from a bug I could reproduce, and
ships with a regression test that fails without the fix.

| Project | Change | Status |
|---|---|---|
| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx/pull/3850) | Streaming zipformer and keyword spotting produced no output on SME2-capable ARM cores | merged |
| [ml-explore/mlx](https://github.com/ml-explore/mlx/pull/4096) | `mx.compile` could return another function's result after a cross-thread release | open |
| [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm/pull/1697) | Fine-tuning loss counted one padding token per sequence | open |
| [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm/pull/1698) | GLM applied RoPE over the full head dimension instead of the partial factor | open |
| [huggingface/tokenizers](https://github.com/huggingface/tokenizers/pull/2327) | BPE training emitted a merge for a pair occurring zero times | open |
| [speechbrain/speechbrain](https://github.com/speechbrain/speechbrain/pull/3073) | Relative positional encoding could not distinguish forward from backward | open |
| [pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio/pull/2046) | Diarization pulled a gated checkpoint it then discarded | open |
| [chroma-core/chroma](https://github.com/chroma-core/chroma/pull/7574) | `n_results=0` panicked the local HNSW reader | open |
| [chroma-core/hnswlib](https://github.com/chroma-core/hnswlib/pull/47) | An unvalidated link-list size grew the index file without bound | open |
| [pytorch/torchtitan](https://github.com/pytorch/torchtitan/pull/4109) | Least-loaded routing never rotated between tied candidates | open |
| [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm/pull/1844) | Server responses were identical across requests unless a seed was set | open |

---

### Working with

Speech and audio — VoxCPM, Spark-TTS, Whisper and Qwen3-ASR fine-tuning, VAD,
diarization, forced alignment, codec and channel simulation.

Training — PyTorch, LoRA and full fine-tunes, multi-GPU (FSDP, DDP), MLX on Apple
silicon.

Serving — vLLM, CTranslate2, ONNX Runtime, sherpa-onnx, batched custom runtimes.

---

mr.yentur@gmail.com
