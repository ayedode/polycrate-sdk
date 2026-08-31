from typing import Literal

ApiV1ArtifactsCreateSpecErrorComponentAttr = Literal["spec"]

API_V1_ARTIFACTS_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateSpecErrorComponentAttr] = {
    "spec",
}


def check_api_v1_artifacts_create_spec_error_component_attr(value: str) -> ApiV1ArtifactsCreateSpecErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
