from typing import Literal

ApiV1AgentsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_AGENTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AgentsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_agents_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1AgentsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_AGENTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
