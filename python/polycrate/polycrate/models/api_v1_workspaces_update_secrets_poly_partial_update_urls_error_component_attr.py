from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponentAttr = Literal["urls"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_urls_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateUrlsErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
