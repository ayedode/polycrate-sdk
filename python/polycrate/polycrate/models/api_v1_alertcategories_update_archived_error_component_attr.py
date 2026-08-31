from typing import Literal

ApiV1AlertcategoriesUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ALERTCATEGORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_alertcategories_update_archived_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateArchivedErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
