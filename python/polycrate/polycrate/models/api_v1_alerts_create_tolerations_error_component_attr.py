from typing import Literal

ApiV1AlertsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateTolerationsErrorComponentAttr] = {
    "tolerations",
}


def check_api_v1_alerts_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertsCreateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
