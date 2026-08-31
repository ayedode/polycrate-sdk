from typing import Literal

ApiV1DowntimesCreateExcludedReasonErrorComponentAttr = Literal["excluded_reason"]

API_V1_DOWNTIMES_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesCreateExcludedReasonErrorComponentAttr
] = {
    "excluded_reason",
}


def check_api_v1_downtimes_create_excluded_reason_error_component_attr(
    value: str,
) -> ApiV1DowntimesCreateExcludedReasonErrorComponentAttr:
    if value in API_V1_DOWNTIMES_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
