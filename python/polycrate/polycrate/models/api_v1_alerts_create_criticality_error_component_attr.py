from typing import Literal

ApiV1AlertsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ALERTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_alerts_create_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertsCreateCriticalityErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
