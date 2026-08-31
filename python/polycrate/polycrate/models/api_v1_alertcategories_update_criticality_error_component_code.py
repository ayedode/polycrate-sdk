from typing import Literal

ApiV1AlertcategoriesUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTCATEGORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alertcategories_update_criticality_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateCriticalityErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
