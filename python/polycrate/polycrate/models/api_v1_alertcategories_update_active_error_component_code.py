from typing import Literal

ApiV1AlertcategoriesUpdateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTCATEGORIES_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertcategories_update_active_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateActiveErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
