from typing import Literal

ApiV1NotesCreateProjectIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_NOTES_CREATE_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateProjectIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_notes_create_project_id_error_component_code(
    value: str,
) -> ApiV1NotesCreateProjectIdErrorComponentCode:
    if value in API_V1_NOTES_CREATE_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
