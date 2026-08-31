from typing import Literal

ApiV1AgentsCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_AGENTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AgentsCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_agents_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1AgentsCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_AGENTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
