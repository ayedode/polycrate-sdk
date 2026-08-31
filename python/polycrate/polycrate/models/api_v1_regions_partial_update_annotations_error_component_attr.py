from typing import Literal

ApiV1RegionsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_REGIONS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_regions_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
