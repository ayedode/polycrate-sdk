from typing import Literal

ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_rescan_provider_status_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
