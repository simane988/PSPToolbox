# PSP Video Converter
A small Python script for automatically converting video files into a format compatible with the PlayStation Portable (PSP), including thumbnail generation. Supports all PSP models, including TV-out mode.

[Русский](README) | [English](README_EN)

## Features
- Converts all videos from `input_videos` into `.mp4` files playable on PSP
- Generates a `.thm` thumbnail for each video (by default from the 1st second)
- Docker-based deployment
- Automatically selects optimal settings based on PSP model
- Supports TV mode (`720x480`) for video output via AV/component cable

## Quick Start

### 1. Build the Docker image:
```bash
docker build -t psp-converter .
````

### 2. Prepare folders:
Create `input_videos` and `output_videos` folders next to the `Dockerfile`, and place your videos into `input_videos`.

### 3. Run the container:
```bash
docker run --rm \
  -v $(pwd)/input_videos:/app/input_videos \
  -v $(pwd)/output_videos:/app/output_videos \
  -e PSP_MODEL=3000 \
  psp-converter
```

### 4. (Optional) Enable TV mode:
```bash
-e TV_OUT=true
```
This sets the video resolution to `720x480` so it can be played on a TV using the PSP's video output feature.

## Supported PSP Models
| PSP Model | Default Resolution | Video Bitrate | CRF | TV Output Support |
| --------- | ------------------ | ------------- | --- | ----------------- |
| `1000`    | 368×208            | 768k          | 25  | ❌                 |
| `2000`    | 480×272 / 720×480  | 1024k         | 23  | ✅                 |
| `3000`    | 480×272 / 720×480  | 1500k         | 21  | ✅                 |

> ⚠️ PSP-1000 has strict decoding limitations: it doesn't support videos above 368×208 or H.264 above Level 1.3.

## Environment Variables
| Variable               | Description                                                                            | Default Value |
| ---------------------- |----------------------------------------------------------------------------------------| ------------- |
| `PSP_MODEL`            | PSP model: `1000`, `2000`, or `3000`                                                   | `1000`        |
| `TV_OUT`               | Set to `true` to enable 720×480 resolution for TV output (only works on PSP 2000/3000) | `false`       |
| `PSP_RESOLUTION`       | Manually override output resolution                                                    | auto          |
| `PSP_CRF`              | CRF (quality, from 0 (best) to 51 (worst))                                             | auto          |
| `PSP_VIDEO_BITRATE`    | Video bitrate (e.g. `1024k`)                                                           | auto          |
| `PSP_AUDIO_BITRATE`    | Audio bitrate (e.g. `128k`)                                                            | `128k`        |
| `PSP_AUDIO_HZ`         | Audio frequency (e.g. `48000`)                                                         | `48000`       |
| `PSP_THUMBNAIL_SECOND` | Second at which the frame is captured for thumbnail generation                         | `1`           |

## Output Files
* `.mp4` video files compatible with PSP
* `.thm` thumbnails generated from the specified second

## Credits
Thanks to the [VidToPSP-ffmpeg](https://github.com/wanesty/VidToPSP-ffmpeg) project by [wanesty](https://github.com/wanesty),
which inspired this script and provided the base ffmpeg parameters.