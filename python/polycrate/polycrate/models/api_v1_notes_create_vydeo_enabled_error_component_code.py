from typing import Literal

ApiV1NotesCreateVydeoEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateVydeoEnabledErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_notes_create_vydeo_enabled_error_component_code(
    value: str,
) -> ApiV1NotesCreateVydeoEnabledErrorComponentCode:
    if value in API_V1_NOTES_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
