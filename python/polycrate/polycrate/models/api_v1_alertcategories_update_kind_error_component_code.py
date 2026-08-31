from typing import Literal

ApiV1AlertcategoriesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTCATEGORIES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alertcategories_update_kind_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateKindErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
