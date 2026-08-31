from typing import Literal

ApiV1NotesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesCreateTolerationsErrorComponentAttr] = {
    "tolerations",
}


def check_api_v1_notes_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1NotesCreateTolerationsErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
