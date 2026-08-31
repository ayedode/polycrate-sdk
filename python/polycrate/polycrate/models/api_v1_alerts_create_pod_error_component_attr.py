from typing import Literal

ApiV1AlertsCreatePodErrorComponentAttr = Literal["pod"]

API_V1_ALERTS_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreatePodErrorComponentAttr] = {
    "pod",
}


def check_api_v1_alerts_create_pod_error_component_attr(value: str) -> ApiV1AlertsCreatePodErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
