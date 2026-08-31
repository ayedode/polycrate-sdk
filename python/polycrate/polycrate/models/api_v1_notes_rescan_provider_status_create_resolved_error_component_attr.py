from typing import Literal

ApiV1NotesRescanProviderStatusCreateResolvedErrorComponentAttr = Literal["resolved"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateResolvedErrorComponentAttr
] = {
    "resolved",
}


def check_api_v1_notes_rescan_provider_status_create_resolved_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateResolvedErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
