from typing import Literal

ApiV1NotesUpdateProjectIdErrorComponentAttr = Literal["project_id"]

API_V1_NOTES_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateProjectIdErrorComponentAttr] = {
    "project_id",
}


def check_api_v1_notes_update_project_id_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateProjectIdErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
