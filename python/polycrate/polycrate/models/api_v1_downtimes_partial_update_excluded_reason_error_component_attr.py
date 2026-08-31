from typing import Literal

ApiV1DowntimesPartialUpdateExcludedReasonErrorComponentAttr = Literal["excluded_reason"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesPartialUpdateExcludedReasonErrorComponentAttr
] = {
    "excluded_reason",
}


def check_api_v1_downtimes_partial_update_excluded_reason_error_component_attr(
    value: str,
) -> ApiV1DowntimesPartialUpdateExcludedReasonErrorComponentAttr:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
