from typing import Literal

ApiV1AlertcategoryMappingsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_ALERTCATEGORY_MAPPINGS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryMappingsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_alertcategory_mappings_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1AlertcategoryMappingsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
