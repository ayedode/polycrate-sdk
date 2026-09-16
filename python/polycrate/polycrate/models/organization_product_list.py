from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_product_list_active_condition_instances_item import (
        OrganizationProductListActiveConditionInstancesItem,
    )
    from ..models.organization_product_list_created import OrganizationProductListCreated
    from ..models.organization_product_list_organization_type_0 import OrganizationProductListOrganizationType0
    from ..models.organization_product_list_workspace_type_0 import OrganizationProductListWorkspaceType0
    from ..models.product_simple import ProductSimple


T = TypeVar("T", bound="OrganizationProductList")


@_attrs_define
class OrganizationProductList:
    """List serializer for V2 table views.

    Attributes:
        id (UUID):
        name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        labels (Any):
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
            Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
        active_condition_instances (list[OrganizationProductListActiveConditionInstancesItem]):
        organization (None | OrganizationProductListOrganizationType0):
        organization_priority (bool): True when the object's organization has priority=True.
        workspace (None | OrganizationProductListWorkspaceType0):
        created (OrganizationProductListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        reconciliation_running (bool):
        effective_criticality (EffectiveCriticalityEnum | None):
        url (str): Gibt die absolute URL zum Object zurück.
        product (ProductSimple): Compact serializer for embedding Product as FK reference.
        agreed_price (str):
        active_from (datetime.date | None | Unset):
        active_until (datetime.date | None | Unset):
        auto_managed (bool | Unset):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[OrganizationProductListActiveConditionInstancesItem]
    organization: None | OrganizationProductListOrganizationType0
    organization_priority: bool
    workspace: None | OrganizationProductListWorkspaceType0
    created: OrganizationProductListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    product: ProductSimple
    agreed_price: str
    active_from: datetime.date | None | Unset = UNSET
    active_until: datetime.date | None | Unset = UNSET
    auto_managed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_product_list_organization_type_0 import (
            OrganizationProductListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.organization_product_list_workspace_type_0 import (
            OrganizationProductListWorkspaceType0,  # noqa: PLC0415
        )

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: dict[str, Any] | None
        if isinstance(self.organization, OrganizationProductListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, OrganizationProductListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        product = self.product.to_dict()

        agreed_price = self.agreed_price

        active_from: None | str | Unset
        if isinstance(self.active_from, Unset):
            active_from = UNSET
        elif isinstance(self.active_from, datetime.date):
            active_from = self.active_from.isoformat()
        else:
            active_from = self.active_from

        active_until: None | str | Unset
        if isinstance(self.active_until, Unset):
            active_until = UNSET
        elif isinstance(self.active_until, datetime.date):
            active_until = self.active_until.isoformat()
        else:
            active_until = self.active_until

        auto_managed = self.auto_managed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "product": product,
                "agreed_price": agreed_price,
            }
        )
        if active_from is not UNSET:
            field_dict["active_from"] = active_from
        if active_until is not UNSET:
            field_dict["active_until"] = active_until
        if auto_managed is not UNSET:
            field_dict["auto_managed"] = auto_managed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_product_list_active_condition_instances_item import (
            OrganizationProductListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.organization_product_list_created import OrganizationProductListCreated  # noqa: PLC0415
        from ..models.organization_product_list_organization_type_0 import (
            OrganizationProductListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.organization_product_list_workspace_type_0 import (
            OrganizationProductListWorkspaceType0,  # noqa: PLC0415
        )
        from ..models.product_simple import ProductSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = OrganizationProductListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | OrganizationProductListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = OrganizationProductListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationProductListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | OrganizationProductListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = OrganizationProductListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationProductListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = OrganizationProductListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        product = ProductSimple.from_dict(d.pop("product"))

        agreed_price = d.pop("agreed_price")

        def _parse_active_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_from_type_0 = datetime.date.fromisoformat(data)

                return active_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_from = _parse_active_from(d.pop("active_from", UNSET))

        def _parse_active_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_until_type_0 = datetime.date.fromisoformat(data)

                return active_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_until = _parse_active_until(d.pop("active_until", UNSET))

        auto_managed = d.pop("auto_managed", UNSET)

        organization_product_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            product=product,
            agreed_price=agreed_price,
            active_from=active_from,
            active_until=active_until,
            auto_managed=auto_managed,
        )

        organization_product_list.additional_properties = d
        return organization_product_list

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
