from typing import Literal

ApiV1PoliciesDryRunCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_policies_dry_run_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
