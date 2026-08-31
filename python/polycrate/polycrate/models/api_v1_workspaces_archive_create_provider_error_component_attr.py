from typing import Literal

ApiV1WorkspacesArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_workspaces_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
