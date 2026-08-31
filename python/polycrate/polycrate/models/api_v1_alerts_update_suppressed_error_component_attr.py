from typing import Literal

ApiV1AlertsUpdateSuppressedErrorComponentAttr = Literal["suppressed"]

API_V1_ALERTS_UPDATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateSuppressedErrorComponentAttr] = {
    "suppressed",
}


def check_api_v1_alerts_update_suppressed_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateSuppressedErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
