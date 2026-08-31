from typing import Literal

ApiV1DowntimesUpdateExcludedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOWNTIMES_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesUpdateExcludedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_downtimes_update_excluded_reason_error_component_code(
    value: str,
) -> ApiV1DowntimesUpdateExcludedReasonErrorComponentCode:
    if value in API_V1_DOWNTIMES_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_EXCLUDED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
