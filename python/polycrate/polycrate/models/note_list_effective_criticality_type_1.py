from typing import Literal

NoteListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

NOTE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[NoteListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_note_list_effective_criticality_type_1(value: str) -> NoteListEffectiveCriticalityType1:
    if value in NOTE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
