from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponentAttr = Literal["pop_id"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponentAttr
] = {
    "pop_id",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_pop_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePopIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
