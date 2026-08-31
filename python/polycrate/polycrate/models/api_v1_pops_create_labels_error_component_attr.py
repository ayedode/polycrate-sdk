from typing import Literal

ApiV1PopsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_POPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_pops_create_labels_error_component_attr(value: str) -> ApiV1PopsCreateLabelsErrorComponentAttr:
    if value in API_V1_POPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
