from typing import Literal

ApiV1DowntimesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_update_tolerations_error_component_code(
    value: str,
) -> ApiV1DowntimesUpdateTolerationsErrorComponentCode:
    if value in API_V1_DOWNTIMES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
