from typing import Literal

ApiV1NotesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_NOTES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_notes_create_labels_error_component_attr(value: str) -> ApiV1NotesCreateLabelsErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
