from typing import Literal

ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponentAttr = Literal["remind_at"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_REMIND_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponentAttr
] = {
    "remind_at",
}


def check_api_v1_notes_rescan_provider_status_create_remind_at_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_REMIND_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_REMIND_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
