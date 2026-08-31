from typing import Literal

ApiV1CvesPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CVES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesPartialUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_cves_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
