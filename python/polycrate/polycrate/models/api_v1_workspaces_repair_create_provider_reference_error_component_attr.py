from typing import Literal

ApiV1WorkspacesRepairCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_WORKSPACES_REPAIR_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_workspaces_repair_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
