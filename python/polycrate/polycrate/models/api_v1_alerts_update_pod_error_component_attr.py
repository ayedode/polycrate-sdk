from typing import Literal

ApiV1AlertsUpdatePodErrorComponentAttr = Literal["pod"]

API_V1_ALERTS_UPDATE_POD_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdatePodErrorComponentAttr] = {
    "pod",
}


def check_api_v1_alerts_update_pod_error_component_attr(value: str) -> ApiV1AlertsUpdatePodErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
