from typing import Literal

ApiV1AlertroutersCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ALERTROUTERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_alertrouters_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateArchivedAtErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
