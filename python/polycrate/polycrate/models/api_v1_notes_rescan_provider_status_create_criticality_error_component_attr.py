from typing import Literal

ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_notes_rescan_provider_status_create_criticality_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
