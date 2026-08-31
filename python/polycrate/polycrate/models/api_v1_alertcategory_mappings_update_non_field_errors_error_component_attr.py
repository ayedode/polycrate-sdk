from typing import Literal

ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_alertcategory_mappings_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
