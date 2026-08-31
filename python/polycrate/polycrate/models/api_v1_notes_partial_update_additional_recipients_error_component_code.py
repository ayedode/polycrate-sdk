from typing import Literal

ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_PARTIAL_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_partial_update_additional_recipients_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
