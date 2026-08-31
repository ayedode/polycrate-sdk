from typing import Literal

ApiV1NotesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_NOTES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_notes_update_kind_error_component_attr(value: str) -> ApiV1NotesUpdateKindErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
