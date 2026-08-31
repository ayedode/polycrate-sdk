from typing import Literal

ApiV1MaintenancesCreateDraftErrorComponentAttr = Literal["draft"]

API_V1_MAINTENANCES_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesCreateDraftErrorComponentAttr] = {
    "draft",
}


def check_api_v1_maintenances_create_draft_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateDraftErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
