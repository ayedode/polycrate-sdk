from typing import Literal

ApiV1CvesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CVES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_cves_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
