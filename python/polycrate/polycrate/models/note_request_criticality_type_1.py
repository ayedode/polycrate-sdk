from typing import Literal

NoteRequestCriticalityType1 = Literal["", "high", "low", "medium"]

NOTE_REQUEST_CRITICALITY_TYPE_1_VALUES: set[NoteRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_note_request_criticality_type_1(value: str) -> NoteRequestCriticalityType1:
    if value in NOTE_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
