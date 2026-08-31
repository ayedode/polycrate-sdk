from typing import Literal

ApiV1PopsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_POPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_pops_update_labels_error_component_attr(value: str) -> ApiV1PopsUpdateLabelsErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
