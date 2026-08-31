from typing import Literal

ApiV1WorkspacesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_WORKSPACES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_workspaces_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
