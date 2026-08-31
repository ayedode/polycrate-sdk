from typing import Literal

ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_artifact_repositories_update_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
