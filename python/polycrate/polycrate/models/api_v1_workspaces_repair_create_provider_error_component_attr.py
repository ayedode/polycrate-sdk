from typing import Literal

ApiV1WorkspacesRepairCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_REPAIR_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_workspaces_repair_create_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
