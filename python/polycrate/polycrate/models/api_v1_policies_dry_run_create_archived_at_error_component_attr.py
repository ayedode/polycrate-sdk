from typing import Literal

ApiV1PoliciesDryRunCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_policies_dry_run_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateArchivedAtErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
