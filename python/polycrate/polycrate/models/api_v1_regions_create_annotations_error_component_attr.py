from typing import Literal

ApiV1RegionsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_REGIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsCreateAnnotationsErrorComponentAttr] = {
    "annotations",
}


def check_api_v1_regions_create_annotations_error_component_attr(
    value: str,
) -> ApiV1RegionsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
