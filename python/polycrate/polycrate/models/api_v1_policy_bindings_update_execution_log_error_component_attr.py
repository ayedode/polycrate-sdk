from typing import Literal

ApiV1PolicyBindingsUpdateExecutionLogErrorComponentAttr = Literal["execution_log"]

API_V1_POLICY_BINDINGS_UPDATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsUpdateExecutionLogErrorComponentAttr
] = {
    "execution_log",
}


def check_api_v1_policy_bindings_update_execution_log_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsUpdateExecutionLogErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_UPDATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_UPDATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
