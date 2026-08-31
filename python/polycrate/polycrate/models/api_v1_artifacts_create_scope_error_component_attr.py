from typing import Literal

ApiV1ArtifactsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ARTIFACTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_artifacts_create_scope_error_component_attr(value: str) -> ApiV1ArtifactsCreateScopeErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
