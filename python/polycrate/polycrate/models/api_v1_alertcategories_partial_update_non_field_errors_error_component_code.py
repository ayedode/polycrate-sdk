from typing import Literal

ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertcategories_partial_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
