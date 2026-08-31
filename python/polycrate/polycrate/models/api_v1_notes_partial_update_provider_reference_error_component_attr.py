from typing import Literal

ApiV1NotesPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_NOTES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_notes_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
