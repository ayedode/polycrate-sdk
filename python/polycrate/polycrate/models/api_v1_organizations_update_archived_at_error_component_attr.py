from typing import Literal

ApiV1OrganizationsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ORGANIZATIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_organizations_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
