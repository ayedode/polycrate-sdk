from typing import Literal

ApiV1AlertsDiscoverCreatePodErrorComponentAttr = Literal["pod"]

API_V1_ALERTS_DISCOVER_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsDiscoverCreatePodErrorComponentAttr] = {
    "pod",
}


def check_api_v1_alerts_discover_create_pod_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreatePodErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
