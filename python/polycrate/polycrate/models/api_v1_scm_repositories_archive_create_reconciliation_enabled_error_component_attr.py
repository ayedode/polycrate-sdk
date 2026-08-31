from typing import Literal

ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_scm_repositories_archive_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
