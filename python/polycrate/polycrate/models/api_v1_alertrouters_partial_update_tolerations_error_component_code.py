from typing import Literal

ApiV1AlertroutersPartialUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersPartialUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_partial_update_tolerations_error_component_code(
    value: str,
) -> ApiV1AlertroutersPartialUpdateTolerationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
