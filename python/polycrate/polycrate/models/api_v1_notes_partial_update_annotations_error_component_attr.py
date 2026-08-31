from typing import Literal

ApiV1NotesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_NOTES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_notes_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
