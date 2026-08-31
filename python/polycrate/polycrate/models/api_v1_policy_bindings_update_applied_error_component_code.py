from typing import Literal

ApiV1PolicyBindingsUpdateAppliedErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_UPDATE_APPLIED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsUpdateAppliedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_update_applied_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsUpdateAppliedErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_UPDATE_APPLIED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_UPDATE_APPLIED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
