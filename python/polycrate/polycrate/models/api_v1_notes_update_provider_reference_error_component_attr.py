from typing import Literal

ApiV1NotesUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_NOTES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_notes_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
