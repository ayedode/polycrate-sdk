from typing import Literal

ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notes_rescan_provider_status_create_annotations_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
