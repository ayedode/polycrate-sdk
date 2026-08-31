from typing import Literal

ApiV1ProjectsUpdateProductIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PROJECTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsUpdateProductIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_projects_update_product_id_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdateProductIdErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
