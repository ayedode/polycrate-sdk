from typing import Literal

ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_rescan_provider_status_create_structured_content_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
