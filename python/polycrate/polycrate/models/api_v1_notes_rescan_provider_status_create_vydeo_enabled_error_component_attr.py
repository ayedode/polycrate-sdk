from typing import Literal

ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponentAttr = Literal["vydeo_enabled"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponentAttr
] = {
    "vydeo_enabled",
}


def check_api_v1_notes_rescan_provider_status_create_vydeo_enabled_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
