from typing import Literal

ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_datasources_rescan_notes_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
