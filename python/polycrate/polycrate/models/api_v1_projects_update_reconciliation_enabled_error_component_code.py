from typing import Literal

ApiV1ProjectsUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
