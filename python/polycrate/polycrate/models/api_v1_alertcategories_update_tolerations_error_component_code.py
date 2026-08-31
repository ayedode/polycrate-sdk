from typing import Literal

ApiV1AlertcategoriesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTCATEGORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertcategories_update_tolerations_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateTolerationsErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
