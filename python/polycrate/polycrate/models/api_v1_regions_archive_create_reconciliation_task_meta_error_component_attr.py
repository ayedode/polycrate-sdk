from typing import Literal

ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponentAttr = Literal["reconciliation_task_meta"]

API_V1_REGIONS_ARCHIVE_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponentAttr
] = {
    "reconciliation_task_meta",
}


def check_api_v1_regions_archive_create_reconciliation_task_meta_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
