from typing import Literal

ApiV1ConditionsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CONDITIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_conditions_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
