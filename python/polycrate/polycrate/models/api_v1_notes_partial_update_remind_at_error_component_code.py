from typing import Literal

ApiV1NotesPartialUpdateRemindAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_NOTES_PARTIAL_UPDATE_REMIND_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateRemindAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_notes_partial_update_remind_at_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateRemindAtErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_REMIND_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_REMIND_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
