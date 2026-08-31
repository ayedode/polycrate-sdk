from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponentAttr = Literal["alternative_name"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponentAttr
] = {
    "alternative_name",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_alternative_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateAlternativeNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
