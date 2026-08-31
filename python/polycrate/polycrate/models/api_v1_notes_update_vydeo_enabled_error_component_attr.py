from typing import Literal

ApiV1NotesUpdateVydeoEnabledErrorComponentAttr = Literal["vydeo_enabled"]

API_V1_NOTES_UPDATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateVydeoEnabledErrorComponentAttr] = {
    "vydeo_enabled",
}


def check_api_v1_notes_update_vydeo_enabled_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateVydeoEnabledErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
