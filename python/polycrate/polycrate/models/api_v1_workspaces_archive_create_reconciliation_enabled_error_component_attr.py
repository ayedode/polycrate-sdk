from typing import Literal

ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_WORKSPACES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_workspaces_archive_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
