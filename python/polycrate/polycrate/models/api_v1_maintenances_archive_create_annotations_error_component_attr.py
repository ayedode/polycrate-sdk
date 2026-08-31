from typing import Literal

ApiV1MaintenancesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_maintenances_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
