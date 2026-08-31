from typing import Literal

ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_scm_repositories_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
