from typing import Literal

ApiV1NotesPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_NOTES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesPartialUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_notes_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateNameErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
