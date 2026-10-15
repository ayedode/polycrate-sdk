from typing import Literal

NoteListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

NOTE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[NoteListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_note_list_effective_criticality_type_3_type_1(value: str) -> NoteListEffectiveCriticalityType3Type1:
    if value in NOTE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
