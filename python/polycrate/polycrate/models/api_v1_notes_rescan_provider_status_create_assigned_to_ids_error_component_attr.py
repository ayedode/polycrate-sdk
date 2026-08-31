from typing import Literal

ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponentAttr = Literal["assigned_to_ids"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponentAttr
] = {
    "assigned_to_ids",
}


def check_api_v1_notes_rescan_provider_status_create_assigned_to_ids_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
