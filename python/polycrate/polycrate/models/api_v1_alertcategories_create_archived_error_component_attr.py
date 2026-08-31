from typing import Literal

ApiV1AlertcategoriesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_alertcategories_create_archived_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateArchivedErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
