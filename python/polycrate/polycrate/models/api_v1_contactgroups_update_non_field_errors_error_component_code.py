from typing import Literal

ApiV1ContactgroupsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_CONTACTGROUPS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactgroupsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_contactgroups_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ContactgroupsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
