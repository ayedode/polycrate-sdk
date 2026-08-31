from typing import Literal

ApiV1RegionsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_REGIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_regions_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
