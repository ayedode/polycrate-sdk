from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cost_statement_line_item_usage_row import CostStatementLineItemUsageRow


T = TypeVar("T", bound="CostStatementLineItem")


@_attrs_define
class CostStatementLineItem:
    """Read-only. LineItems are never written directly (only via generate action).

    Attributes:
        id (UUID):
        organization_product (None | UUID):
        product_kind (str):
        product_name (str):
        resource_name (str):
        workspace (None | UUID):
        workspace_name (str):
        unit_price (str):
        billing_interval (str):
        quantity (str):
        total_net (str):
        active_from (datetime.datetime | None):
        active_until (datetime.datetime | None):
        prorated (bool):
        prorate_factor (str):
        usage_rows (list[CostStatementLineItemUsageRow]):
    """

    id: UUID
    organization_product: None | UUID
    product_kind: str
    product_name: str
    resource_name: str
    workspace: None | UUID
    workspace_name: str
    unit_price: str
    billing_interval: str
    quantity: str
    total_net: str
    active_from: datetime.datetime | None
    active_until: datetime.datetime | None
    prorated: bool
    prorate_factor: str
    usage_rows: list[CostStatementLineItemUsageRow]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        organization_product: None | str
        if isinstance(self.organization_product, UUID):
            organization_product = str(self.organization_product)
        else:
            organization_product = self.organization_product

        product_kind = self.product_kind

        product_name = self.product_name

        resource_name = self.resource_name

        workspace: None | str
        if isinstance(self.workspace, UUID):
            workspace = str(self.workspace)
        else:
            workspace = self.workspace

        workspace_name = self.workspace_name

        unit_price = self.unit_price

        billing_interval = self.billing_interval

        quantity = self.quantity

        total_net = self.total_net

        active_from: None | str
        if isinstance(self.active_from, datetime.datetime):
            active_from = self.active_from.isoformat()
        else:
            active_from = self.active_from

        active_until: None | str
        if isinstance(self.active_until, datetime.datetime):
            active_until = self.active_until.isoformat()
        else:
            active_until = self.active_until

        prorated = self.prorated

        prorate_factor = self.prorate_factor

        usage_rows = []
        for usage_rows_item_data in self.usage_rows:
            usage_rows_item = usage_rows_item_data.to_dict()
            usage_rows.append(usage_rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization_product": organization_product,
                "product_kind": product_kind,
                "product_name": product_name,
                "resource_name": resource_name,
                "workspace": workspace,
                "workspace_name": workspace_name,
                "unit_price": unit_price,
                "billing_interval": billing_interval,
                "quantity": quantity,
                "total_net": total_net,
                "active_from": active_from,
                "active_until": active_until,
                "prorated": prorated,
                "prorate_factor": prorate_factor,
                "usage_rows": usage_rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_statement_line_item_usage_row import CostStatementLineItemUsageRow

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_organization_product(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_product_type_0 = UUID(data)

                return organization_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        organization_product = _parse_organization_product(d.pop("organization_product"))

        product_kind = d.pop("product_kind")

        product_name = d.pop("product_name")

        resource_name = d.pop("resource_name")

        def _parse_workspace(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_type_0 = UUID(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        workspace = _parse_workspace(d.pop("workspace"))

        workspace_name = d.pop("workspace_name")

        unit_price = d.pop("unit_price")

        billing_interval = d.pop("billing_interval")

        quantity = d.pop("quantity")

        total_net = d.pop("total_net")

        def _parse_active_from(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_from_type_0 = datetime.datetime.fromisoformat(data)

                return active_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        active_from = _parse_active_from(d.pop("active_from"))

        def _parse_active_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_until_type_0 = datetime.datetime.fromisoformat(data)

                return active_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        active_until = _parse_active_until(d.pop("active_until"))

        prorated = d.pop("prorated")

        prorate_factor = d.pop("prorate_factor")

        usage_rows = []
        _usage_rows = d.pop("usage_rows")
        for usage_rows_item_data in _usage_rows:
            usage_rows_item = CostStatementLineItemUsageRow.from_dict(usage_rows_item_data)

            usage_rows.append(usage_rows_item)

        cost_statement_line_item = cls(
            id=id,
            organization_product=organization_product,
            product_kind=product_kind,
            product_name=product_name,
            resource_name=resource_name,
            workspace=workspace,
            workspace_name=workspace_name,
            unit_price=unit_price,
            billing_interval=billing_interval,
            quantity=quantity,
            total_net=total_net,
            active_from=active_from,
            active_until=active_until,
            prorated=prorated,
            prorate_factor=prorate_factor,
            usage_rows=usage_rows,
        )

        cost_statement_line_item.additional_properties = d
        return cost_statement_line_item

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
