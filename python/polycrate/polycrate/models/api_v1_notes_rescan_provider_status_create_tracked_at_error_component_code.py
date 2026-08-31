from typing import Literal

ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_notes_rescan_provider_status_create_tracked_at_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
