from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_run_discovery_create_provider_reference_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateProviderReferenceErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
