from typing import Literal

ApiV1NotesRescanProviderStatusCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_notes_rescan_provider_status_create_labels_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateLabelsErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
