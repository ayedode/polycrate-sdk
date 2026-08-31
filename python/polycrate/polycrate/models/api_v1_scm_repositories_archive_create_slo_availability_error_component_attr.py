from typing import Literal

ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_scm_repositories_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
