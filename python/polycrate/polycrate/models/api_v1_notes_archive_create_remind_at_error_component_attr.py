from typing import Literal

ApiV1NotesArchiveCreateRemindAtErrorComponentAttr = Literal["remind_at"]

API_V1_NOTES_ARCHIVE_CREATE_REMIND_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateRemindAtErrorComponentAttr
] = {
    "remind_at",
}


def check_api_v1_notes_archive_create_remind_at_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateRemindAtErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_REMIND_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_REMIND_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
