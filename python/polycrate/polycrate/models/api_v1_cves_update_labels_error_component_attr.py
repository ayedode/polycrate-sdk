from typing import Literal

ApiV1CvesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CVES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_cves_update_labels_error_component_attr(value: str) -> ApiV1CvesUpdateLabelsErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
