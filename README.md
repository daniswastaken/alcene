<picture>
  <source
    width="100%"
    srcset="./docs/banner.avif"
    media="(prefers-color-scheme: dark)"
  />
  <source
    width="100%"
    srcset="./docs/banner.avif"
    media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"
  />
  <img width="100%" src="./docs/banner.avif" alt="alcene.ai banner" />
</picture>

<h1 align="center">MNIST — alcene.ai</h1>

<p align="center">Lightweight embedded MNIST model built from the ground up.</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-22c55e?style=flat&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJtMTYgMTYgMy04IDMgOGMtLjg3LjY1LTEuOTIgMS0zIDFzLTIuMTMtLjM1LTMtMVoiLz48cGF0aCBkPSJtMiAxNiAzLTggMyA4Yy0uODcuNjUtMS45MiAxLTMgMXMtMi4xMy0uMzUtMy0xWiIvPjxwYXRoIGQ9Ik03IDIxaDEwIi8+PHBhdGggZD0iTTEyIDN2MTgiLz48cGF0aCBkPSJNMyA3aDJjMiAwIDUtMSA3LTIgMiAxIDUgMiA3IDJoMiIvPjwvc3ZnPg==&logoColor=white&labelColor=1a1024" />
  <img alt="Status" src="https://img.shields.io/badge/Status-Pre--Launch-8b5cf6?style=flat&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNNC41IDE2LjVjLTEuNSAxLjI2LTIgNS0yIDVzMy43NC0uNSA1LTJjLjcxLS44NC43LTIuMTMtLjA5LTIuOTFhMi4xOCAyLjE4IDAgMCAwLTIuOTEtLjA5eiIvPjxwYXRoIGQ9Im0xMiAxNS0zLTNhMjIgMjIgMCAwIDEgMi0zLjk1QTEyLjg4IDEyLjg4IDAgMCAxIDIyIDJjMCAyLjcyLS43OCA3LjUtNiAxMWEyMi4zNSAyMi4zNSAwIDAgMS00IDJ6Ii8+PHBhdGggZD0iTTkgMTJINHMuNTUtMy4wMyAyLTRjMS42Mi0xLjA4IDUgMCA1IDAiLz48cGF0aCBkPSJNMTIgMTV2NXMzLjAzLS41NSA0LTJjMS4wOC0xLjYyIDAtNSAwLTUiLz48L3N2Zz4=&logoColor=white&labelColor=1a1024" />
  <img alt="Scope" src="https://img.shields.io/badge/Scope-Embedded%20Inference-3b82f6?style=flat&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNNCA2YTIgMiAwIDAgMSAyLTJoMTJhMiAyIDAgMCAxIDIgMnYxMmEyIDIgMCAwIDEtMiAySDZhMiAyIDAgMCAxLTItMnoiLz48cGF0aCBkPSJNOSA5aDZ2Nkg5eiIvPjxwYXRoIGQ9Ik0xNSAydjIiLz48cGF0aCBkPSJNMTUgMjB2MiIvPjxwYXRoIGQ9Ik0yIDE1aDIiLz48cGF0aCBkPSJNMiA5aDIiLz48cGF0aCBkPSJNMjAgMTVoMiIvPjxwYXRoIGQ9Ik0yMCA5aDIiLz48cGF0aCBkPSJNOSAydjIiLz48cGF0aCBkPSJNOSAyMHYyIi8+PC9zdmc+&logoColor=white&labelColor=1a1024" />
  <img alt="Footprint" src="https://img.shields.io/badge/Footprint-Lightweight-f97316?style=flat&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWdvbiBwb2ludHM9IjEzIDIgMyAxNCAxMiAxNCAxMSAyMiAyMSAxMCAxMiAxMCAxMyAyIi8+PC9zdmc+&logoColor=white&labelColor=1a1024" />
</p>

> [!NOTE]
> `MNIST — alcene.ai` is a **sub-AI** from `alcene.ai`. This branch contains all the codes and data setup needed to build and train the **Alcene's MNIST** model from scratch.

> [!TIP]
> **Alcene's MNIST** model are trained and designed to run fully locally on **ESP32 S3** or any other capable embedded inference.

## What Is This Branch About?

This branch is focused on training and making an **MNIST** model. MNIST model itself are an AI trained to guess a digit from the provided `28x28 pixels image`.

- Benchmarks: **~97.58%** accuracy across 20000 image tests.
- Layers: **3-layers** neural network.
- Weights: `< 1 MB` model weight.

> [!IMPORTANT]
> The MNIST model is currently still in progress to be brought onto `ESP32 S3` platform.

## License

MIT — see [`LICENSE`](LICENSE). Copyright (c) 2026 Handaru Daniswara.

## Star History

<a href="https://star-history.com/#daniswastaken/alcene&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=daniswastaken/alcene&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=daniswastaken/alcene&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=daniswastaken/alcene&type=Date" />
  </picture>
</a>
