from typing import Literal

ApiV1BackupsBackupsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_BACKUPS_BACKUPS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_backups_backups_list_organizations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListOrganizationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
