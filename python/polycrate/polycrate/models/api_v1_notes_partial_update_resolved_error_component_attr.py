from typing import Literal

ApiV1NotesPartialUpdateResolvedErrorComponentAttr = Literal["resolved"]

API_V1_NOTES_PARTIAL_UPDATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateResolvedErrorComponentAttr
] = {
    "resolved",
}


def check_api_v1_notes_partial_update_resolved_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateResolvedErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
