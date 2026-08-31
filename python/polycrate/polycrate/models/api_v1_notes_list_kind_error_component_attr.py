from typing import Literal

ApiV1NotesListKindErrorComponentAttr = Literal["kind"]

API_V1_NOTES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_notes_list_kind_error_component_attr(value: str) -> ApiV1NotesListKindErrorComponentAttr:
    if value in API_V1_NOTES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
