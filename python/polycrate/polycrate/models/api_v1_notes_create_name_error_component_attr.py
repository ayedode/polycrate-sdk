from typing import Literal

ApiV1NotesCreateNameErrorComponentAttr = Literal["name"]

API_V1_NOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_notes_create_name_error_component_attr(value: str) -> ApiV1NotesCreateNameErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
