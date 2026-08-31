from typing import Literal

ApiV1PoliciesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_POLICIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_policies_update_labels_error_component_attr(value: str) -> ApiV1PoliciesUpdateLabelsErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
