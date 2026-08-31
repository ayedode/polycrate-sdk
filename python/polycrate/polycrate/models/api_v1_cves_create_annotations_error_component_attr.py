from typing import Literal

ApiV1CvesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CVES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateAnnotationsErrorComponentAttr] = {
    "annotations",
}


def check_api_v1_cves_create_annotations_error_component_attr(
    value: str,
) -> ApiV1CvesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CVES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
