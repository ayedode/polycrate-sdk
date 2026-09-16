from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.ip_family_enum import IPFamilyEnum, check_ip_family_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.purpose_ff_5_enum import PurposeFf5Enum, check_purpose_ff_5_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prefix_list_active_condition_instances_item import PrefixListActiveConditionInstancesItem
    from ..models.prefix_list_created import PrefixListCreated
    from ..models.prefix_list_organization_type_0 import PrefixListOrganizationType0
    from ..models.prefix_list_workspace_type_0 import PrefixListWorkspaceType0


T = TypeVar("T", bound="PrefixList")


@_attrs_define
class PrefixList:
    """Lightweight serializer for Prefix list views.
    Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectListSerializer.
    organization/workspace automatisch von ManagedObjectListSerializer.

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
            active_condition_instances (list[PrefixListActiveConditionInstancesItem]):
            organization (None | PrefixListOrganizationType0):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | PrefixListWorkspaceType0):
            created (PrefixListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            cidr (str): Prefix CIDR, e.g. 192.168.1.0/24
            kind (IPFamilyEnum | Unset): * `ipv4` - IPv4
                * `ipv6` - IPv6
            purpose (PurposeFf5Enum | Unset): * `loadbalancer` - Load Balancer
                * `controlplane` - Controlplane
            description (str | Unset): Description of the prefix
            region (None | Unset | UUID): Region this prefix belongs to. Required when purpose=controlplane.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[PrefixListActiveConditionInstancesItem]
    organization: None | PrefixListOrganizationType0
    organization_priority: bool
    workspace: None | PrefixListWorkspaceType0
    created: PrefixListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    cidr: str
    kind: IPFamilyEnum | Unset = UNSET
    purpose: PurposeFf5Enum | Unset = UNSET
    description: str | Unset = UNSET
    region: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prefix_list_organization_type_0 import PrefixListOrganizationType0  # noqa: PLC0415
        from ..models.prefix_list_workspace_type_0 import PrefixListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, PrefixListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, PrefixListWorkspaceType0):
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

        cidr = self.cidr

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose

        description = self.description

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        elif isinstance(self.region, UUID):
            region = str(self.region)
        else:
            region = self.region

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
                "cidr": cidr,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if description is not UNSET:
            field_dict["description"] = description
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prefix_list_active_condition_instances_item import (
            PrefixListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.prefix_list_created import PrefixListCreated  # noqa: PLC0415
        from ..models.prefix_list_organization_type_0 import PrefixListOrganizationType0  # noqa: PLC0415
        from ..models.prefix_list_workspace_type_0 import PrefixListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = PrefixListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | PrefixListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = PrefixListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrefixListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | PrefixListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = PrefixListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrefixListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = PrefixListCreated.from_dict(d.pop("created"))

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

        cidr = d.pop("cidr")

        _kind = d.pop("kind", UNSET)
        kind: IPFamilyEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_ip_family_enum(_kind)

        _purpose = d.pop("purpose", UNSET)
        purpose: PurposeFf5Enum | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = check_purpose_ff_5_enum(_purpose)

        description = d.pop("description", UNSET)

        def _parse_region(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                region_type_0 = UUID(data)

                return region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        region = _parse_region(d.pop("region", UNSET))

        prefix_list = cls(
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
            cidr=cidr,
            kind=kind,
            purpose=purpose,
            description=description,
            region=region,
        )

        prefix_list.additional_properties = d
        return prefix_list

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
