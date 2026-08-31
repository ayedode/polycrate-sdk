from typing import Literal

ApiV1ArtifactsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_ARTIFACTS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_artifacts_update_scope_error_component_attr(value: str) -> ApiV1ArtifactsUpdateScopeErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
