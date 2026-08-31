from typing import Literal

ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_rescan_provider_status_create_vydeo_enabled_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
