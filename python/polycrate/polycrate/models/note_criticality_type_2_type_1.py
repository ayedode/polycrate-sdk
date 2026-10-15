from typing import Literal

NoteCriticalityType2Type1 = Literal["", "high", "low", "medium"]

NOTE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[NoteCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_note_criticality_type_2_type_1(value: str) -> NoteCriticalityType2Type1:
    if value in NOTE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
