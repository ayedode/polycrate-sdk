from typing import Literal

ApiV1PoliciesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POLICIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PoliciesCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_policies_create_kind_error_component_code(value: str) -> ApiV1PoliciesCreateKindErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
