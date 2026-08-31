from typing import Literal

ApiV1AlertroutersUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTROUTERS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertroutersUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alertrouters_update_kind_error_component_code(
    value: str,
) -> ApiV1AlertroutersUpdateKindErrorComponentCode:
    if value in API_V1_ALERTROUTERS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
