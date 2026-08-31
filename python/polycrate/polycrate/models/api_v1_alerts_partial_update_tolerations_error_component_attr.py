from typing import Literal

ApiV1AlertsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_alerts_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
