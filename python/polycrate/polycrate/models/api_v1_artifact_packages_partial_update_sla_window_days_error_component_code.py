from typing import Literal

ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_artifact_packages_partial_update_sla_window_days_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateSlaWindowDaysErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
