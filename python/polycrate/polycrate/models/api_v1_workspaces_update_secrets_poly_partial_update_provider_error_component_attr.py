from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
