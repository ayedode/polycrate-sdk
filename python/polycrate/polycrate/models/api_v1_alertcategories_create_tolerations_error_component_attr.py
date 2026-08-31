from typing import Literal

ApiV1AlertcategoriesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTCATEGORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_alertcategories_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
