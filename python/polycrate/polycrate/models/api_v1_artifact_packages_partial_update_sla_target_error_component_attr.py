from typing import Literal

ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_artifact_packages_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
