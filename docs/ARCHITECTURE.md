# Laboratory Architecture

```text
External model/data
        ↓
   Organism Adapter
        ↓
   Standard Interface
        ↓
  Experiment Runner
        ↓
 Metrics / Logs / State
        ↓
   Reproducible Result
```

## Separation

**External:** опубликованные модели и данные.

**Adapter:** наш технический слой совместимости.

**Experiment:** конкретная проверка с фиксированной конфигурацией.

**Result:** только измеренный результат запуска.

Это позволяет сравнивать разные цифровые организмы одной методикой.
