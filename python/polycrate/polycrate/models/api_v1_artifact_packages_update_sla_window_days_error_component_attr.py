from typing import Literal

ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_ARTIFACT_PACKAGES_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_artifact_packages_update_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
