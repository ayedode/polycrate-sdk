from typing import Literal

ApiV1NotesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_NOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesCreateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_notes_create_criticality_error_component_attr(
    value: str,
) -> ApiV1NotesCreateCriticalityErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
