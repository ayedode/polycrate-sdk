from typing import Literal

ApiV1DowntimesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_downtimes_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DowntimesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
