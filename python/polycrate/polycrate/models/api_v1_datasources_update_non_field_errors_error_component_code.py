from typing import Literal

ApiV1DatasourcesUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
