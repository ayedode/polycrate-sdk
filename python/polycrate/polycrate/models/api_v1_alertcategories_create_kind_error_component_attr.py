from typing import Literal

ApiV1AlertcategoriesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ALERTCATEGORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_alertcategories_create_kind_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateKindErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
