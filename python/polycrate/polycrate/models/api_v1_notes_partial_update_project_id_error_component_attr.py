from typing import Literal

ApiV1NotesPartialUpdateProjectIdErrorComponentAttr = Literal["project_id"]

API_V1_NOTES_PARTIAL_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateProjectIdErrorComponentAttr
] = {
    "project_id",
}


def check_api_v1_notes_partial_update_project_id_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateProjectIdErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
