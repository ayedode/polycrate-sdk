from typing import Literal

ApiV1DowntimesCreateExcludedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOWNTIMES_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesCreateExcludedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_downtimes_create_excluded_reason_error_component_code(
    value: str,
) -> ApiV1DowntimesCreateExcludedReasonErrorComponentCode:
    if value in API_V1_DOWNTIMES_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
