from typing import Literal

ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_artifact_repositories_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
