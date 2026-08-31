from typing import Literal

ApiV1NotesPartialUpdateVydeoEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_PARTIAL_UPDATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateVydeoEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_partial_update_vydeo_enabled_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateVydeoEnabledErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_VYDEO_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
