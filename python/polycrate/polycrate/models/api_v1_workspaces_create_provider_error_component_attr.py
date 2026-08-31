from typing import Literal

ApiV1WorkspacesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_workspaces_create_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
