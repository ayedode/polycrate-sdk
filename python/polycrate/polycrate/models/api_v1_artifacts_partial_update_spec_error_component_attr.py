from typing import Literal

ApiV1ArtifactsPartialUpdateSpecErrorComponentAttr = Literal["spec"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateSpecErrorComponentAttr
] = {
    "spec",
}


def check_api_v1_artifacts_partial_update_spec_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateSpecErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
