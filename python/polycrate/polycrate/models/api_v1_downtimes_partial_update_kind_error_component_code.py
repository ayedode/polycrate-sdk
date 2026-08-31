from typing import Literal

ApiV1DowntimesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_downtimes_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1DowntimesPartialUpdateKindErrorComponentCode:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
