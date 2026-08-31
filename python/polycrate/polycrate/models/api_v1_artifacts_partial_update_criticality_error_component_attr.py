from typing import Literal

ApiV1ArtifactsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifacts_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
