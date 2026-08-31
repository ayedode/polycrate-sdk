from typing import Literal

ApiV1RegionsPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_REGIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_regions_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
