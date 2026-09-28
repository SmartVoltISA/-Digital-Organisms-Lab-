# DOL-E000 — Baseline

## Purpose

Проверить локальный экспериментальный контур до подключения биологической модели.

## Model

`examples/minimal_organism.py`

## Hypothesis

Замкнутый контур `state → environment → action → feedback` должен быть воспроизводим локально.

## Null

При одинаковых параметрах и seed состояние может отличаться.

## Metrics

- final position
- final energy
- number of steps

## Status

Engineering baseline. Не биологический результат.

## Next

Подключить первую реальную модель C. elegans через адаптер.
