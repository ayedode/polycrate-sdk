from typing import Literal

ApiV1AlertsPartialUpdateSuppressedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_PARTIAL_UPDATE_SUPPRESSED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateSuppressedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_partial_update_suppressed_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateSuppressedErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_SUPPRESSED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_SUPPRESSED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
