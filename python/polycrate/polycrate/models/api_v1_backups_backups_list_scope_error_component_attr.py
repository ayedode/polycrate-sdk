from typing import Literal

ApiV1BackupsBackupsListScopeErrorComponentAttr = Literal["scope"]

API_V1_BACKUPS_BACKUPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BackupsBackupsListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_backups_backups_list_scope_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListScopeErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
