from typing import Literal

ApiV1NotesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_NOTES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_notes_create_provider_error_component_attr(value: str) -> ApiV1NotesCreateProviderErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
