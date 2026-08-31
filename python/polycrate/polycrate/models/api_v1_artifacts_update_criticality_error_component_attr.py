from typing import Literal

ApiV1ArtifactsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifacts_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
