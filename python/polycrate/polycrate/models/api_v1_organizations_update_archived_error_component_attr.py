from typing import Literal

ApiV1OrganizationsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ORGANIZATIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_organizations_update_archived_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateArchivedErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
