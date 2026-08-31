from typing import Literal

ApiV1ArtifactsArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_artifacts_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
