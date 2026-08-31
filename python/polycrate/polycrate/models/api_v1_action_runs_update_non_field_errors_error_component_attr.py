from typing import Literal

ApiV1ActionRunsUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_ACTION_RUNS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ActionRunsUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_action_runs_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1ActionRunsUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
