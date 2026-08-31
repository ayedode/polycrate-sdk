from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_interval_enum import BillingIntervalEnum, check_billing_interval_enum
from ..models.product_kind_enum import ProductKindEnum, check_product_kind_enum

T = TypeVar("T", bound="ProductSimple")


@_attrs_define
class ProductSimple:
    """Compact serializer for embedding Product as FK reference.

    Attributes:
        id (UUID):
        name (str):
        display_name (None | str): The display name is used to display the object in the UI. It can be different from
            the name.
        kind (ProductKindEnum): * `host` - Host
            * `k8scluster` - K8s Cluster
            * `k8sapp` - K8s App
            * `support` - Support
            * `object-storage` - Object Storage
            * `block-storage` - Block Storage
            * `loadbalancer` - Loadbalancer
            * `project` - Project
            * `dnszone` - DNS Zone
            * `assistant` - Assistant
        billing_interval (BillingIntervalEnum): * `second` - Second
            * `minute` - Minute
            * `hour` - Hour
            * `day` - Day
            * `month` - Month
            * `year` - Year
        price_per_unit (None | str):
        url (str):
    """

    id: UUID
    name: str
    display_name: None | str
    kind: ProductKindEnum
    billing_interval: BillingIntervalEnum
    price_per_unit: None | str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        kind: str = self.kind

        billing_interval: str = self.billing_interval

        price_per_unit: None | str
        price_per_unit = self.price_per_unit

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "kind": kind,
                "billing_interval": billing_interval,
                "price_per_unit": price_per_unit,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        kind = check_product_kind_enum(d.pop("kind"))

        billing_interval = check_billing_interval_enum(d.pop("billing_interval"))

        def _parse_price_per_unit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        price_per_unit = _parse_price_per_unit(d.pop("price_per_unit"))

        url = d.pop("url")

        product_simple = cls(
            id=id,
            name=name,
            display_name=display_name,
            kind=kind,
            billing_interval=billing_interval,
            price_per_unit=price_per_unit,
            url=url,
        )

        product_simple.additional_properties = d
        return product_simple

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
