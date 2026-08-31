from typing import Literal

ApiV1DowntimesUpdateExcludedReasonErrorComponentAttr = Literal["excluded_reason"]

API_V1_DOWNTIMES_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesUpdateExcludedReasonErrorComponentAttr
] = {
    "excluded_reason",
}


def check_api_v1_downtimes_update_excluded_reason_error_component_attr(
    value: str,
) -> ApiV1DowntimesUpdateExcludedReasonErrorComponentAttr:
    if value in API_V1_DOWNTIMES_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
