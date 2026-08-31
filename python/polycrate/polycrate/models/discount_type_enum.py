from typing import Literal

DiscountTypeEnum = Literal["fixed_override", "fixed_reduction", "percentage"]

DISCOUNT_TYPE_ENUM_VALUES: set[DiscountTypeEnum] = {
    "fixed_override",
    "fixed_reduction",
    "percentage",
}


def check_discount_type_enum(value: str) -> DiscountTypeEnum:
    if value in DISCOUNT_TYPE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DISCOUNT_TYPE_ENUM_VALUES!r}")
