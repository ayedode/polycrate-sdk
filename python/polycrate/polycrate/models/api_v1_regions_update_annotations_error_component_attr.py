from typing import Literal

ApiV1RegionsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsUpdateAnnotationsErrorComponentAttr] = {
    "annotations",
}


def check_api_v1_regions_update_annotations_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
