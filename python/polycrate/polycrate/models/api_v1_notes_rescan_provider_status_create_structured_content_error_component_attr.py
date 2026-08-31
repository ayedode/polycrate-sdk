from typing import Literal

ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponentAttr = Literal["structured_content"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponentAttr
] = {
    "structured_content",
}


def check_api_v1_notes_rescan_provider_status_create_structured_content_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
