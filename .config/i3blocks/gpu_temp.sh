#~/bin/#!/usr/bin/env bash
GPU=$(nvidia-smi --format=nounits,csv,noheader --query-gpu=temperature.gpu)

# Full and short texts
echo "GPU Temp: $GPU"

exit 0
