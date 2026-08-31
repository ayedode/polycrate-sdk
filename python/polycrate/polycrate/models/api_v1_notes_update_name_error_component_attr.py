from typing import Literal

ApiV1NotesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_NOTES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_notes_update_name_error_component_attr(value: str) -> ApiV1NotesUpdateNameErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
