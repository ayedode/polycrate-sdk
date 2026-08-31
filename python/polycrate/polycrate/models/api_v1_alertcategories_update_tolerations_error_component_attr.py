from typing import Literal

ApiV1AlertcategoriesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTCATEGORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_alertcategories_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
