from typing import Literal

ApiV1AlertsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_alerts_create_labels_error_component_attr(value: str) -> ApiV1AlertsCreateLabelsErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
