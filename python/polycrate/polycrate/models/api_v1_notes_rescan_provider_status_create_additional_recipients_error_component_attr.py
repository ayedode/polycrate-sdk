from typing import Literal

ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponentAttr = Literal["additional_recipients"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponentAttr
] = {
    "additional_recipients",
}


def check_api_v1_notes_rescan_provider_status_create_additional_recipients_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
