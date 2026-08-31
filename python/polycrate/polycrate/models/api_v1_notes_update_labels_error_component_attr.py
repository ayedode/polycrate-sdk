from typing import Literal

ApiV1NotesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_NOTES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_notes_update_labels_error_component_attr(value: str) -> ApiV1NotesUpdateLabelsErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
