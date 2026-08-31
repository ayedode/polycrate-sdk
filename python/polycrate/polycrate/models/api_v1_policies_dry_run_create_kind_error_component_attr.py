from typing import Literal

ApiV1PoliciesDryRunCreateKindErrorComponentAttr = Literal["kind"]

API_V1_POLICIES_DRY_RUN_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_policies_dry_run_create_kind_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateKindErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
