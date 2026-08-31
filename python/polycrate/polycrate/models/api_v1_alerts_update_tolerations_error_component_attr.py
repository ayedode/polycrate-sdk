from typing import Literal

ApiV1AlertsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateTolerationsErrorComponentAttr] = {
    "tolerations",
}


def check_api_v1_alerts_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
