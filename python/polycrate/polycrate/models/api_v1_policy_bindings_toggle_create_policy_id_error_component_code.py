from typing import Literal

ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_POLICY_BINDINGS_TOGGLE_CREATE_POLICY_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_policy_bindings_toggle_create_policy_id_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_TOGGLE_CREATE_POLICY_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_TOGGLE_CREATE_POLICY_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
