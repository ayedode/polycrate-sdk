from typing import Literal

ApiV1CvesCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_CVES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_cves_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1CvesCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_CVES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
