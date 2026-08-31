from typing import Literal

ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
