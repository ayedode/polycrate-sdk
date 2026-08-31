from typing import Literal

ApiV1AlertroutersCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTROUTERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertroutersCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alertrouters_create_kind_error_component_code(
    value: str,
) -> ApiV1AlertroutersCreateKindErrorComponentCode:
    if value in API_V1_ALERTROUTERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
