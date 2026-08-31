from typing import Literal

ApiV1CvesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CVES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_cves_create_labels_error_component_attr(value: str) -> ApiV1CvesCreateLabelsErrorComponentAttr:
    if value in API_V1_CVES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
