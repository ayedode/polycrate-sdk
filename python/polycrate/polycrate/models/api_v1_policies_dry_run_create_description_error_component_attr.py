from typing import Literal

ApiV1PoliciesDryRunCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_POLICIES_DRY_RUN_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_policies_dry_run_create_description_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateDescriptionErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
