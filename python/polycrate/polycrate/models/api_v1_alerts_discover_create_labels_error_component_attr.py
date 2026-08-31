from typing import Literal

ApiV1AlertsDiscoverCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_alerts_discover_create_labels_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateLabelsErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
