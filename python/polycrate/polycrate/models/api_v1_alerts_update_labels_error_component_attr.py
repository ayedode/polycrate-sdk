from typing import Literal

ApiV1AlertsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_alerts_update_labels_error_component_attr(value: str) -> ApiV1AlertsUpdateLabelsErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
