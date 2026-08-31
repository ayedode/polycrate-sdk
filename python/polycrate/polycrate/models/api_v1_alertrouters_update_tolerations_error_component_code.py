from typing import Literal

ApiV1AlertroutersUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_update_tolerations_error_component_code(
    value: str,
) -> ApiV1AlertroutersUpdateTolerationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
