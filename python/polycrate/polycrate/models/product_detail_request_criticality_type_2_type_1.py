from typing import Literal

ProductDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProductDetailRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_product_detail_request_criticality_type_2_type_1(value: str) -> ProductDetailRequestCriticalityType2Type1:
    if value in PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
