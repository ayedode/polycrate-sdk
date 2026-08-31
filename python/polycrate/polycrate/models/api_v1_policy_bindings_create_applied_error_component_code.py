from typing import Literal

ApiV1PolicyBindingsCreateAppliedErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_CREATE_APPLIED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsCreateAppliedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_create_applied_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsCreateAppliedErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_CREATE_APPLIED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_CREATE_APPLIED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
