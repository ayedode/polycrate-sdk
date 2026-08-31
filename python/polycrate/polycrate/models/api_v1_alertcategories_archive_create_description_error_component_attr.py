from typing import Literal

ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_alertcategories_archive_create_description_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
