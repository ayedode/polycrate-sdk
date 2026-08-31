from typing import Literal

ApiV1AlertcategoriesPartialUpdateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertcategories_partial_update_active_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateActiveErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
