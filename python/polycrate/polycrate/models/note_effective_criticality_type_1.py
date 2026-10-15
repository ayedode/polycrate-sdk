from typing import Literal

NoteEffectiveCriticalityType1 = Literal["high", "low", "medium"]

NOTE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[NoteEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_note_effective_criticality_type_1(value: str) -> NoteEffectiveCriticalityType1:
    if value in NOTE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
