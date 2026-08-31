from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
