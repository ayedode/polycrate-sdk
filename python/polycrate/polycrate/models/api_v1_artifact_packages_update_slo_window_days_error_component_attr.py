from typing import Literal

ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_ARTIFACT_PACKAGES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_artifact_packages_update_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
