from typing import Literal

ApiV1NotesRescanProviderStatusCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_notes_rescan_provider_status_create_provider_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateProviderErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
