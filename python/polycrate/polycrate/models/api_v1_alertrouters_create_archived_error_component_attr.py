from typing import Literal

ApiV1AlertroutersCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ALERTROUTERS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_alertrouters_create_archived_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateArchivedErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
