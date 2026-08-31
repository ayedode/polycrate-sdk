from typing import Literal

ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponentAttr = Literal["execution_log"]

API_V1_POLICY_BINDINGS_TOGGLE_CREATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponentAttr
] = {
    "execution_log",
}


def check_api_v1_policy_bindings_toggle_create_execution_log_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_TOGGLE_CREATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_TOGGLE_CREATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
