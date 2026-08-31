from typing import Literal

ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_notes_rescan_provider_status_create_display_name_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
