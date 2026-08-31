from typing import Literal

ApiV1RegionsUpdateReconciliationTaskIdErrorComponentAttr = Literal["reconciliation_task_id"]

API_V1_REGIONS_UPDATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsUpdateReconciliationTaskIdErrorComponentAttr
] = {
    "reconciliation_task_id",
}


def check_api_v1_regions_update_reconciliation_task_id_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdateReconciliationTaskIdErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
