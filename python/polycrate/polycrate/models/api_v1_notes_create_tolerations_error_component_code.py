from typing import Literal

ApiV1NotesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateTolerationsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_notes_create_tolerations_error_component_code(
    value: str,
) -> ApiV1NotesCreateTolerationsErrorComponentCode:
    if value in API_V1_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
