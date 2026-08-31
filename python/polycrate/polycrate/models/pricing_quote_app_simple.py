from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_simple import ProductSimple


T = TypeVar("T", bound="PricingQuoteAppSimple")


@_attrs_define
class PricingQuoteAppSimple:
    """
    Attributes:
        id (UUID):
        product (ProductSimple): Compact serializer for embedding Product as FK reference.
        catalogue_app (None | UUID):
        count (int):
        quoted_price (None | str):
    """

    id: UUID
    product: ProductSimple
    catalogue_app: None | UUID
    count: int
    quoted_price: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        product = self.product.to_dict()

        catalogue_app: None | str
        if isinstance(self.catalogue_app, UUID):
            catalogue_app = str(self.catalogue_app)
        else:
            catalogue_app = self.catalogue_app

        count = self.count

        quoted_price: None | str
        quoted_price = self.quoted_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product": product,
                "catalogue_app": catalogue_app,
                "count": count,
                "quoted_price": quoted_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_simple import ProductSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        product = ProductSimple.from_dict(d.pop("product"))

        def _parse_catalogue_app(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                catalogue_app_type_0 = UUID(data)

                return catalogue_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        catalogue_app = _parse_catalogue_app(d.pop("catalogue_app"))

        count = d.pop("count")

        def _parse_quoted_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        quoted_price = _parse_quoted_price(d.pop("quoted_price"))

        pricing_quote_app_simple = cls(
            id=id,
            product=product,
            catalogue_app=catalogue_app,
            count=count,
            quoted_price=quoted_price,
        )

        pricing_quote_app_simple.additional_properties = d
        return pricing_quote_app_simple

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
