from typing import Literal

NoteEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

NOTE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[NoteEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_note_effective_criticality_type_3_type_1(value: str) -> NoteEffectiveCriticalityType3Type1:
    if value in NOTE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
