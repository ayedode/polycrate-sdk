from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponentAttr = Literal["on_premise"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponentAttr
] = {
    "on_premise",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_on_premise_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateOnPremiseErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
