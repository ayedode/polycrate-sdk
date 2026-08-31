from typing import Literal

ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponentAttr = Literal["additional_recipients"]

API_V1_NOTES_PARTIAL_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponentAttr
] = {
    "additional_recipients",
}


def check_api_v1_notes_partial_update_additional_recipients_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
