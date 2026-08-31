from typing import Literal

ApiV1AlertsPartialUpdateSuppressedErrorComponentAttr = Literal["suppressed"]

API_V1_ALERTS_PARTIAL_UPDATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateSuppressedErrorComponentAttr
] = {
    "suppressed",
}


def check_api_v1_alerts_partial_update_suppressed_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateSuppressedErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
