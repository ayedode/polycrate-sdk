from typing import Literal

ApiV1NotesRescanProviderStatusCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_notes_rescan_provider_status_create_provider_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateProviderErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
