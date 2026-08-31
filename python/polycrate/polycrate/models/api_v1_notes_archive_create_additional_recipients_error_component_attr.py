from typing import Literal

ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponentAttr = Literal["additional_recipients"]

API_V1_NOTES_ARCHIVE_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponentAttr
] = {
    "additional_recipients",
}


def check_api_v1_notes_archive_create_additional_recipients_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
